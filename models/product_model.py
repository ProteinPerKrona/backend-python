# Imports
from pydantic import BaseModel

class Product(BaseModel):
    name:str
    ppk:float