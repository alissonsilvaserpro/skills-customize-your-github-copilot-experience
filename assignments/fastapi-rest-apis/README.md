# 📘 Task: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of items. This assignment will help you practice creating routes, handling JSON payloads, validating input, and returning structured responses.

## 📝 Tasks

### 🛠️ Create the API App

#### Descrição
Create a FastAPI application that exposes a simple homepage endpoint and a basic in-memory data store for products.

#### Requisitos
O programa concluído deve:

- Create an instance of `FastAPI`.
- Add a root route (`/`) that returns a welcome message.
- Store data in memory using a Python dictionary.
- Ensure the app can run locally with `uvicorn`.

### 🛠️ Read and Filter Items

#### Descrição
Implement endpoints to list all items and retrieve a single item by ID.

#### Requisitos
O programa concluído deve:

- Add a `GET /items` route that returns all items.
- Add a `GET /items/{item_id}` route that returns one item.
- Return a `404` response when an item is not found.
- Use JSON-friendly Python dictionaries and lists.

### 🛠️ Create New Items

#### Descrição
Add support for creating new items through a POST request using a request body model.

#### Requisitos
O programa concluído deve:

- Define a Pydantic model for an item.
- Add a `POST /items` route that accepts JSON input.
- Validate required fields such as `name` and `price`.
- Return the created item with a unique identifier.

### 🛠️ Improve the API

#### Descrição
Add a few quality-of-life improvements such as validation, update support, and better error handling.

#### Requisitos
O programa concluído deve:

- Implement `PUT /items/{item_id}` to update an existing item.
- Use `HTTPException` for invalid requests and missing resources.
- Keep the API response structure clean and consistent.
- Include at least one example payload in the documentation or comments.

## ✅ Extension Ideas

- Add a `DELETE /items/{item_id}` endpoint.
- Return item counts or summaries from a nested endpoint.
- Add query parameters to filter items by name or price.
- Create a second resource such as `customers` or `orders`.

## 🔎 Suggested Starter Command

```bash
uvicorn starter-code:app --reload
```
