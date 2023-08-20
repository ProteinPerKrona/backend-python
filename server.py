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


@app.get("/test")
def test_db():
    resp = "Server running"
    return resp

@app.get("/protein_percent")
def protein_percente():
    # Filters so that all results have protein over 10
    query_obj = {
        'nutritions.protein':{'$gt':10}
    }
    sortby = 'nutritions.protein'

    products = products_serializer(collection.find(query_obj).limit(10).sort(sortby,pymongo.DESCENDING))
    return products


@app.get("/ppk_10%")
def ppk_10():
    # Filters so that all results have protein over 10
    query_obj = {
        'nutritions.protein':{'$gt':10}
    }
    sortby = 'ppk'
    products = products_serializer(collection.find(query_obj).limit(10).sort(sortby,pymongo.DESCENDING))
    return products


@app.post("/custom_req")
def custom_req(request:Request):

    # Example request to filter for more than 10% protein and order by fat percentege
    '''
    {
    "orderby": "nutritions.fett",
    "filter": {
            "nutritions.protein":{"$gt":10}
        }
    }
    
    '''
    req = request.model_dump()

    query_obj = req['filter']
    orderby = req["orderby"]

    products = products_serializer(collection.find(query_obj).limit(10).sort(orderby,pymongo.DESCENDING))
    return products