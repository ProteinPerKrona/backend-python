# Imports
from pymongo import MongoClient, DESCENDING

# Constants
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "databse"
COLLECTION_NAME = "collection_name"


db_connection = MongoClient(MONGO_URL)
db = db_connection.get_database(DB_NAME)
collection = db.get_collection(COLLECTION_NAME)

def test_db():
    return collection.find({}).limit(10).sort('_id',DESCENDING)

