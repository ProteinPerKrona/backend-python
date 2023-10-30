# Imports
import pymongo

from fastapi import FastAPI, Request


from models.request_model import Request
from schemas.product_schema import products_serializer
from config.db import collection
from fastapi.middleware.cors import CORSMiddleware


# Run by using: uvicorn main:app --reload
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
    right_products = products[(page_length-1)*page_no:page_length*page_no]

    # Returns products
    return right_products


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

    # Selects the right products for the page
    right_products = products[(page_length-1)*page_no:page_length*page_no]

    # Returns products
    return right_products


# @app.get("/ppg/")
# def ppk(number: int = 5, page: int = 1):
#     query_obj = {
#     }
#     sortby = 'nutritions.protein'
#     products = products_serializer(collection.find(query_obj).limit(
#         page*number).sort(sortby, pymongo.DESCENDING))

#     return products[(page-1)*number:page*number]


# @app.post("/custom_req")
# def custom_req(request: Request):

#     # Example request to filter for more than 10% protein and order by fat percentege
#     '''
#     {
#     "orderby": "nutritions.fett",
#     "filter": {
#             "nutritions.protein":{"$gt":10}
#         }
#     }
#     '''
#     req = request.model_dump()

#     query_obj = req['filter']
#     orderby = req["orderby"]

#     products = products_serializer(collection.find(
#         query_obj).limit(10).sort(orderby, pymongo.DESCENDING))

#     return products


# @app.get("/protein_percent")
# def protein_percente():
#     '''Returns a list of products based on protein per 100g'''

#     # Queries for a minimum of 10 percent protein
#     QUERY_OBJ = {'nutritions.protein': {'$gt': 10}}

#     # Sorts by protein percentage
#     SORTBY = 'nutritions.protein'

#     # Queries the database
#     database_products = collection.find(QUERY_OBJ).limit(
#         10).sort(SORTBY, pymongo.DESCENDING)

#     # Serializes products
#     serialized_products = products_serializer(database_products)

#     # Returns products
#     return serialized_products
