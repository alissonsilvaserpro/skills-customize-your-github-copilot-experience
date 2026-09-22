import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI SQLite CRUD")


def get_db_connection():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


class ItemCreate(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQLite CRUD API!"}


@app.get("/items")
def get_items():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return dict(row)


@app.post("/items")
def create_item(item: ItemCreate):
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO items (name, price) VALUES (?, ?)",
        (item.name, item.price),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return {"id": item_id, "name": item.name, "price": item.price}


# Students can add PUT and DELETE endpoints here.
