import json
from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["movies_db"]

with open("sample_data.json") as f:
    movies = json.load(f)
    if db.movies.count_documents({}) == 0: 
        db.movies.insert_many(movies)
        print("Datos insertados correctamente en MongoDB.")
    else:
        print("Los datos ya existen en la base de datos.")
