import imp
from unicodedata import category
from pydantic import BaseModel
from typing import Optional

'''
name: item name
brand: item brand
type: item/mask/movie/tinder/checkout
category: furniture/food
description: item description
model_path: model url or uri
model_location: local/online
model_extras: for movie to load the video
texture_path: item texture path for button
price: item price
'''

class Item(BaseModel):
    name: str
    brand: str
    type: str
    category: str
    description: str
    model_path: str
    model_location: str
    model_extras: str
    texture_path: str
    price: float
    