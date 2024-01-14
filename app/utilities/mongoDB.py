from app import app
from pymongo import MongoClient

def connectMongo(MONGO_URI, DATABASE, COLLECTION):
    try:
        print("Creating connection to Mongo.")
        client = MongoClient(MONGO_URI)
        db = client[DATABASE]
        collection = db[COLLECTION]
        return client, db, collection
    
    except Exception as e:
        raise Exception("[Exception]: {e}")

def closeMongo(client):
    print("Closing Connection to Mongo.")
    client.close()