from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://142502019:Kabaddi@cluster0.epqcybp.mongodb.net/?retryWrites=true&w=majority")
db = client["OnlineRetail"]
collection = db["TransactionCentric"]

#  Read
start = datetime.now()
doc = collection.find_one({"InvoiceNo": "536365"})
print("MongoDB Transaction Read Time:", datetime.now() - start)

# Update
start = datetime.now()
collection.update_one(
    {"InvoiceNo": "536365", "Items.StockCode": "85123A"},
    {"$set": {"Items.$.Quantity": 10}}
)
print("MongoDB Transaction Update Time:", datetime.now() - start)

#  Create
start = datetime.now()
collection.insert_one({
    "InvoiceNo": "TEST999",
    "CustomerID": "99999",
    "Country": "India",
    "InvoiceDate": datetime.now(),
    "Items": [{"StockCode": "NEW1", "Description": "Test Item", "Quantity": 1, "UnitPrice": 99.99}]
})
print("MongoDB Transaction Insert Time:", datetime.now() - start)

# Delete
start = datetime.now()
collection.delete_one({"InvoiceNo": "TEST999"})
print("MongoDB Transaction Delete Time:", datetime.now() - start)