
import os
import pprint
from pymongo import MongoClient, ASCENDING
from pymongo.errors import ConnectionFailure, PyMongoError

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/?maxPoolSize=50&w=1")

def get_client(uri=MONGO_URI):
   
    try:
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)  
        client.admin.command("ping")  
        return client
    except ConnectionFailure as e:
        print("Could not connect to MongoDB:", e)
        raise

def setup_db(client, dbname="online_retail"):
    
    db = client[dbname]
    

    tx = db["invoices"]

    cust = db["customers"]
    
    
    tx.create_index([("InvoiceNo", ASCENDING)], unique=True)
    tx.create_index([("CustomerID", ASCENDING)])
    cust.create_index([("CustomerID", ASCENDING)], unique=True)
    
    return db

def insert_transaction_doc(db, invoice_doc):
    
    try:
        db.invoices.insert_one(invoice_doc)
    except PyMongoError as e:
        print("Insert transaction error:", e)
        raise

def insert_customer_doc(db, customer_doc):
   
    try:
        db.customers.update_one(
            {"CustomerID": customer_doc["CustomerID"]},
            {"$setOnInsert": customer_doc},
            upsert=True
        )
    except PyMongoError as e:
        print("Insert customer error:", e)
        raise

# Example CRUD operations
def find_invoice(db, invoice_no):
    try:
        return db.invoices.find_one({"InvoiceNo": invoice_no})
    except PyMongoError as e:
        print("Find error:", e)
        return None

def update_invoice_item_quantity(db, invoice_no, stockcode, new_qty):
    try:
        res = db.invoices.update_one(
            {"InvoiceNo": invoice_no, "items.StockCode": stockcode},
            {"$set": {"items.$.Quantity": new_qty}}
        )
        return res.modified_count
    except PyMongoError as e:
        print("Update error:", e)
        return 0

def delete_invoice(db, invoice_no):
    try:
        res = db.invoices.delete_one({"InvoiceNo": invoice_no})
        return res.deleted_count
    except PyMongoError as e:
        print("Delete error:", e)
        return 0


if __name__ == "__main__":
    client = get_client()
    db = setup_db(client)
    pprint.pprint(db.list_collection_names())


