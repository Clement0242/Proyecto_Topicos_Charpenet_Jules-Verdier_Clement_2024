from pymongo import MongoClient
import os

def get_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
    client = MongoClient(mongo_uri)
    db = client["movies_db"]
    return db["movies"]
