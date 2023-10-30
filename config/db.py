# Imports
from pymongo import MongoClient

# Constants
CONNECTION_STRING = "mongodb://localhost:27017"
DB_NAME = "Product_db"
COLLECTION_NAME = "Product_info"


client = MongoClient(CONNECTION_STRING)
db = client.get_database(DB_NAME)
collection = db.get_collection(COLLECTION_NAME)


def test_db():
    return collection.find({})
