# Imports
from pymongo import MongoClient
from config import CONNECTION_STRING, DB_NAME, COLLECTION_NAME


client = MongoClient(CONNECTION_STRING)
db = client.get_database(DB_NAME)
collection = db.get_collection(COLLECTION_NAME)


def test_db():
    return collection.find({})
