from fastapi import FastAPI
import sqlite3


con = sqlite3.connect('test.db')
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Form The backend"}


@app.get("/item")
def get_item():
    return {"Hello": "One Item"}

@app.get("/items")
def get_items():
    return {"Hello": "All Items"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q):
    return {"item_id": item_id, "q": q}