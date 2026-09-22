# 📘 Assignment: SQLite and FastAPI CRUD

## 🎯 Objective

Build a small FastAPI application that stores data in a SQLite database and supports the main CRUD operations. Students will practice creating API routes, working with databases, and handling validation and errors in a real web application.

## 📝 Tasks

### 🛠️ Set Up the Database

#### Descrição
Create a SQLite database file and a table for storing products or students. Then connect the FastAPI app to the database.

#### Requisitos
O programa concluído deve:

- Create a SQLite database file named `store.db` or similar.
- Create a table with at least these fields: `id`, `name`, and `price`.
- Use a database connection function so the app can connect safely.
- Ensure the app creates the table when it starts.

### 🛠️ List and Read Records

#### Descrição
Add API routes to return all records and fetch one record by ID.

#### Requisitos
O programa concluído deve:

- Add a `GET /items` route that returns every item in the database.
- Add a `GET /items/{item_id}` route that returns a single item.
- Return a `404` response if the item does not exist.
- Return JSON data in a clean and consistent format.

### 🛠️ Create New Records

#### Descrição
Implement a POST endpoint that accepts incoming JSON and inserts a new record into the database.

#### Requisitos
O programa concluído deve:

- Add a `POST /items` route.
- Accept a JSON payload with required fields like `name` and `price`.
- Validate user input before inserting data.
- Return the created record with a generated ID.

### 🛠️ Update and Delete Records

#### Descrição
Complete the CRUD flow by allowing records to be updated and removed.

#### Requisitos
O programa concluído deve:

- Add a `PUT /items/{item_id}` route to update an item.
- Add a `DELETE /items/{item_id}` route to remove an item.
- Handle missing items with friendly error messages.
- Confirm that the data in the database changes correctly after each operation.

## ✅ Extension Ideas

- Add filters such as searching by name.
- Create a second table like `categories` or `customers`.
- Add a `GET /items/count` endpoint to show how many records exist.
- Use a database model and Pydantic schema for cleaner validation.
