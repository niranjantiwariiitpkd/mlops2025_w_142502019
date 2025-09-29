from pymongo import MongoClient
import time


try:
    client = MongoClient("mongodb://localhost:27017", maxPoolSize=50)
    db = client["uci_online_retail"]
    collection = db["customers"] 
    print("Connected to MongoDB")

    # INSERT
    start = time.time()
    collection.insert_one({
        "CustomerID": 99999,
        "Country": "India",
        "Invoices": []
    })
    print("MongoDB INSERT:", time.time() - start)

    # SELECT
    start = time.time()
    results = list(collection.find({"Country": "India"}))
    print("MongoDB SELECT:", time.time() - start)
    print("Documents:", results)

    # UPDATE
    start = time.time()
    collection.update_one(
        {"CustomerID": 99999},
        {"$set": {"Country": "Bharat"}}
    )
    print("MongoDB UPDATE:", time.time() - start)

    # DELETE
    start = time.time()
    collection.delete_one({"CustomerID": 99999})
    print("MongoDB DELETE:", time.time() - start)

except Exception as e:
    print("MongoDB error:", e)