from fastapi import FastAPI
from app.database.database_manipulation import DatabaseManipulation
import sqlite3
from typing import List


# SQLALCHEMY_DATABASE_URL = "test.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

con = sqlite3.connect('test.db', check_same_thread=False)
database_manipulation = DatabaseManipulation(con)
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Form The backend"}


@app.get("/item")
def get_item():
    return {"Hello": "One Item"}

@app.get("/items")
def get_items(table_name: str):
    try:
        return database_manipulation.selectAny(table_name)
    except Exception as e:
        return e

@app.post("/items")
def insert_items(table_name: str, values: list):
    try:
        # return "Item Added"
        database_manipulation.addAnny(table_name,values)
        return "Item Added"
    except Exception as e:
        return e

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return database_manipulation.getItemById(item_id)