from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# ---------- DATABASE ----------
# SQLite DB (자동 생성)
engine = create_engine("sqlite:///exam.db")
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# ---------- REQUEST MODEL ----------
class ItemRequest(BaseModel):
    title: str
    content: str


# ---------- CRUD ----------
# CREATE
@app.post("/create")
def create_item(item: ItemRequest):
    db = SessionLocal()
    new_item = Item(title=item.title, content=item.content)
    db.add(new_item)
    db.commit()
    return {"message": "Created", "item": item}

# READ
@app.get("/items")
def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    return items

# UPDATE
@app.put("/update/{item_id}")
def update_item(item_id: int, item: ItemRequest):
    db = SessionLocal()
    target = db.query(Item).filter(Item.id == item_id).first()
    target.title = item.title
    target.content = item.content
    db.commit()
    return {"message": "Updated"}

# DELETE
@app.delete("/delete/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    target = db.query(Item).filter(Item.id == item_id).first()
    db.delete(target)
    db.commit()
    return {"message": "Deleted"} 
