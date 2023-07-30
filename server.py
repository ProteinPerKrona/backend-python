# Imports

from typing import Union
from fastapi import FastAPI
from bson import ObjectId

from models.product_model import Product
from schemas.product_schema import product_serializer
from config.db import collection, test_db

app = FastAPI()


@app.get("/test_db")
def test_db():
    return test_db()
