from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://142502019:Kabaddi@cluster0.epqcybp.mongodb.net/?retryWrites=true&w=majority")
db = client["OnlineRetail"]
collection = db["CustomerCentric"]

#  Read
start = datetime.now()
doc = collection.find_one({"CustomerID": "12583.0"})
print("MongoDB Customer Read Time:", datetime.now() - start)

#  Update Country
start = datetime.now()
collection.update_one(
    {"CustomerID": "12583.0"},
    {"$set": {"Country": "India"}}
)
print("MongoDB Customer Update Time:", datetime.now() - start)

#  Add Invoice
start = datetime.now()
collection.update_one(
    {"CustomerID": "12583.0"},
    {"$push": {
        "Invoices": {
            "InvoiceNo": "NEW999",
            "InvoiceDate": datetime.now(),
            "Items": [{"StockCode": "NEW2", "Description": "Extra Item", "Quantity": 2, "UnitPrice": 49.99}]
        }
    }}
)
print("MongoDB Customer Insert Time:", datetime.now() - start)

# Delete
start = datetime.now()
collection.delete_one({"CustomerID": "99999"})
print("MongoDB Customer Delete Time:", datetime.now() - start)