### Introduction

Welcome to the **Casting Agency API** project! This API allows you to manage a collection of books and authors, providing functionalities for creating, retrieving, updating, and deleting book and author records. This project is particularly useful for managing a large library of books and their respective authors, allowing users with different roles to perform various actions based on their permissions.

The project utilizes several technologies and libraries including Flask, SQLAlchemy, and Auth0 for authentication and authorization.

### Project Structure

```
├── app.py                   # Main application entry point
├── auth                     # Authentication and authorization module
│   ├── __init__.py
│   ├── auth.py              # Contains auth functions and decorators
├── models.py                # Database models for SQLAlchemy
├── test_app.py              # Unit tests for API endpoints
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

### Development Setup

To set up the development environment for this project, follow the steps below:

#### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
https://github.com/votrai123/render.git
cd render
```

#### 2. Create a Virtual Environment

Create a virtual environment to manage dependencies:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Install Dependencies

Install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

#### 4. Set Up the Database

Set up the database using SQLAlchemy. You can run the following command to create the necessary tables:

```sh
python
>>> from models import setup_db, db_drop_and_create_all
>>> setup_db(app)
>>> db_drop_and_create_all()
```

#### 5. Configure Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```
AUTH0_DOMAIN=dev-trainv.us.auth0.com
ALGORITHMS=RS256
API_AUDIENCE=capstone
DATABASE_URL=postgresql://my_postgres_9p24_user:iuT5Yz7AmDNTsrsoLNMy6nJuoWmEliFQ@dpg-csh4ln3tq21c73e3fkpg-a.oregon-postgres.render.com/my_postgres_9p24
```

## This is my host deployed
```
https://render-deployment-example-jf0r.onrender.com
```



#### 6. Run the Application

Start the Flask application:

```sh
flask run
```

The application will be available at `http://localhost:5000`.

#### 7. Running Tests

To run the test suite, simply execute:

```sh
python test_app.py
```

This will run all the unit tests defined in `test_app.py` to ensure the API endpoints are functioning correctly.

---

Feel free to copy and adjust this documentation as needed. If you have any further questions or need additional details, just let me know! 😊
---

# API Documentation

## Overview
This API allows you to manage books and authors, including functionalities such as creating, retrieving, updating, and deleting records. 


##### Permissions

Following permissions should be created under created API settings.

* `view:authors`
* `view:books`
* `delete:authors`
* `post:authors`
* `update:authors`
* `update:books`
* `post:books`
* `delete:books`


## Base URL
The base URL for all endpoints is:
```
http://localhost:5000
```

## Authentication
This API uses JWT (JSON Web Token) for authentication. You must include the token in the `Authorization` header for all requests.

```
Authorization: Bearer <your_token>
```

## Endpoints

### 1. Get All Books
- **URL:** `/books`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <your_token>`
- **Permissions:** `view:books`
- **Response:**
  ```json
  {
      "success": true,
      "books": [
          {
              "id": 1,
              "title": "A Brave New World",
              "content": "A novel written in 1931...",
              "type": "Science Fiction",
              "release_date": "2024-11-23T19:07:00.000Z",
              "author_id": 1
          },
          ...
      ]
  }
  ```

### 2. Get All Authors
- **URL:** `/authors`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <your_token>`
- **Permissions:** `view:authors`
- **Response:**
  ```json
  {
      "success": true,
      "authors": [
          {
              "id": 1,
              "name": "Aldous Huxley",
              "age": 69,
              "gender": "Male"
          },
          ...
      ]
  }
  ```

### 3. Create a New Book
- **URL:** `/books`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <your_token>`
  - `Content-Type: application/json`
- **Permissions:** `post:books`
- **Body:**
  ```json
  {
      "title": "A Brave New World",
      "content": "A novel written in 1931...",
      "type": "Science Fiction",
      "release_date": "2024-11-23T19:07:00.000Z",
      "author_id": 1
  }
  ```
- **Response:**
  ```json
  {
      "success": true,
      "book_id": 1
  }
  ```

### 4. Create a New Author
- **URL:** `/authors`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer <your_token>`
  - `Content-Type: application/json`
- **Permissions:** `post:authors`
- **Body:**
  ```json
  {
      "name": "Aldous Huxley",
      "age": 69,
      "gender": "Male"
  }
  ```
- **Response:**
  ```json
  {
      "success": true,
      "author_id": 1
  }
  ```

### 5. Delete a Book
- **URL:** `/books/<book_id>`
- **Method:** `DELETE`
- **Headers:**
  - `Authorization: Bearer <your_token>`
- **Permissions:** `delete:books`
- **Response:**
  ```json
  {
      "success": true,
      "book_id": 1
  }
  ```

### 6. Delete an Author
- **URL:** `/authors/<author_id>`
- **Method:** `DELETE`
- **Headers:**
  - `Authorization: Bearer <your_token>`
- **Permissions:** `delete:authors`
- **Response:**
  ```json
  {
      "success": true,
      "author_id": 1
  }
  ```

### 7. Update a Book
- **URL:** `/books/<book_id>`
- **Method:** `PATCH`
- **Headers:**
  - `Authorization: Bearer <your_token>`
  - `Content-Type: application/json`
- **Permissions:** `update:books`
- **Body:**
  ```json
  {
      "title": "Updated Title",
      "content": "Updated Content",
      "type": "Updated Type",
      "release_date": "2024-12-01",
      "author_id": 1
  }
  ```
- **Response:**
  ```json
  {
      "success": true,
      "book": {
          "id": 1,
          "title": "Updated Title",
          "content": "Updated Content",
          "type": "Updated Type",
          "release_date": "2024-12-01",
          "author_id": 1
      }
  }
  ```

### 8. Update an Author
- **URL:** `/authors/<author_id>`
- **Method:** `PATCH`
- **Headers:**
  - `Authorization: Bearer <your_token>`
  - `Content-Type: application/json`
- **Permissions:** `update:authors`
- **Body:**
  ```json
  {
      "name": "Updated Name",
      "age": 70,
      "gender": "Female"
  }
  ```
- **Response:**
  ```json
  {
      "success": true,
      "author": {
          "id": 1,
          "name": "Updated Name",
          "age": 70,
          "gender": "Female"
      }
  }
  ```

## Error Handling
Errors are returned as JSON objects in the following format:
```json
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The API will return the following error codes:
- `400`: Bad Request
- `401`: Unauthorized
- `404`: Resource Not Found
- `422`: Unprocessable
- `500`: Internal Server Error

---
