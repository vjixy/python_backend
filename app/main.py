from fastapi import FastAPI, File, UploadFile
from app.database.database_manipulation import DatabaseManipulation
import sqlite3
from typing import List
import colorific

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


@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    try:
        palette = colorific.extract_colors(file.file, min_prominence=0.1)
        colors = []
        for p in palette[0]:
            colors.append({"prominence":p[1],"rgb_color":p[0],"hex_color": '#%02x%02x%02x' % p[0]})
        return colors
    except Exception as e:
        return e
    
