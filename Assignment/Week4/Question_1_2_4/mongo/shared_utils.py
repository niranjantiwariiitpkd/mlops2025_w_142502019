from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def get_mongo_client():
    try:
        client = MongoClient("mongodb+srv://142502019:Kabaddi@cluster0.epqcybp.mongodb.net/?retryWrites=true&w=majority", maxPoolSize=50)
        print(" MongoDB connected")
        return client
    except ConnectionFailure as e:
        print(" MongoDB connection failed:", e)
        return None