from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Inventory API")

items = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "description": "Gaming laptop"},
    "2": {"id": "2", "name": "Mouse", "price": 29.99, "description": "Wireless mouse"},
}


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.get("/")
def read_root():
    return {"message": "Welcome to the Inventory API!"}


@app.get("/items")
def get_items():
    # Return all items as a list
    return list(items.values())


@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items")
def create_item(item: Item):
    new_id = str(len(items) + 1)
    new_item = {"id": new_id, **item.model_dump()}
    items[new_id] = new_item
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")

    updated_item = {"id": item_id, **item.model_dump()}
    items[item_id] = updated_item
    return updated_item


# Students can add more endpoints here, such as DELETE or filtering.
