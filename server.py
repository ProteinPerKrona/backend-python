# Imports
import pymongo

from typing import Union
from fastapi import FastAPI
from bson import ObjectId

from models.product_model import Product
from models.request_model import Request
from schemas.product_schema import products_serializer
from config.db import collection, test_db



# uvicorn server:app --reload
app = FastAPI()


@app.get("/db_test")
def test_db():
    products = products_serializer(collection.find().limit(1))
    return products

@app.get("/ppk")
def test_ppk():
    products = products_serializer(collection.find().limit(10).sort('ppk',pymongo.DESCENDING))
    return products

@app.get("/ppk_10")
def ppk_10():
    products = products_serializer(collection.find({'protein':{'$gt':15}}).limit(10).sort('ppk',pymongo.DESCENDING))
    return products

@app.post("/tryme")
def ppk_10(request:Request):
    query_obj = {}
    
    req_obj = request.model_dump()
    for query_key in req_obj.keys():
        # {'protein':{'$gt':15}}
        query_obj[query_key] = {'$gt':req_obj[query_key]}

    products = products_serializer(collection.find(query_obj).limit(10).sort('ppk',pymongo.DESCENDING))
    return products