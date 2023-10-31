# Imports
import pymongo

from fastapi import FastAPI

from models.request_model import Request
from schemas.product_schema import products_serializer
from config.db import collection
from fastapi.middleware.cors import CORSMiddleware


# Run by using: uvicorn server:app --reload
app = FastAPI()

# Add cors policy
origins = [
    "0.0.0.0"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test_db():
    '''Test endpoint'''
    resp = "Server running"
    return resp


@app.get("/ppk")
def ppk(page_length: int = 5, page_no: int = 1):
    '''Returns page_length number of product on the n:th page, 
    Sorted by ppk'''
    # Sort by ppk
    SORTBY = 'ppk'

    # Make db query
    database_products = collection.find({}).limit(
        page_length*page_no).sort(SORTBY, pymongo.DESCENDING)

    # Serialize products
    products = products_serializer(database_products)

    # Selects the right products for the page
    right_products = products[(page_no-1)*page_length:page_no*page_length]

    # Returns products
    return {
        "items": right_products,
        "previous": page_no != 1,
        "next": True  # TODO
    }


@app.get("/cpk")
def ppk(page_length: int = 5, page_no: int = 1):
    '''Returns page_length number of product on the n:th page, 
    Sorted by cpk'''
    # Sort by ppk
    SORTBY = 'cpk'
    # Make db query
    database_products = collection.find({}).limit(
        page_length*page_no).sort(SORTBY, pymongo.DESCENDING)

    # Serialize products
    products = products_serializer(database_products)
    print(products)
    # Selects the right products for the page
    right_products = products[(page_no-1)*page_length:page_length*page_no]

    # Returns products
    return right_products


@app.post("/custom_req")
def custom_req(request: Request):

    # Request object
    req = request.model_dump()

    # Get filter and order
    filter = req['filter']
    orderby = req["orderby"]

    products = products_serializer(collection.find(
        filter).limit(10).sort(orderby, pymongo.DESCENDING))

    return products
