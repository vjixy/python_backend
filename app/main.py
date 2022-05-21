from fastapi import FastAPI, File, UploadFile
from app.database.database_manipulation import DatabaseManipulation
import sqlite3
from typing import List, Dict
import colorific
import webcolors

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


# @app.get("/item")
# def get_item():
#     return {"Hello": "One Item"}

# @app.get("/items")
# def get_items(table_name: str):
#     try:
#         return database_manipulation.selectAny(table_name)
#     except Exception as e:
#         return e

@app.get("/items")
def get_items():
    try:
        return database_manipulation.getItems()
    except Exception as e:
        return e

@app.post("/item")
def insert_item(key: str, values: list):
    try:
        if(key == "166278372972930230"):
            database_manipulation.addAnny("item",values)
            return "Item Added"
        return "Wrong Key !!!"
    except Exception as e:
        return e

@app.post("/items")
def insert_items(key: str, values: List[List]):
    try:
        if(key == "166278372972930230"):
            for value in values:
                database_manipulation.addAnny("item",value)
            return "Items Added"
        return "Wrong Key !!!"
    except Exception as e:
        return e

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return database_manipulation.getItemById(item_id)


@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    try:
        palette = colorific.extract_colors(file.file, min_prominence=0.1)
        colors = []
        for p in palette[0]:
            hex_color = '#%02x%02x%02x' % p[0]
            colors.append({"prominence":p[1],"rgb_color":p[0],"hex_color": hex_color})
        return colors
    except Exception as e:
        return e
    
