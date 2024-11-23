
---

# API Documentation

## Overview
This API allows you to manage books and authors, including functionalities such as creating, retrieving, updating, and deleting records. 

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
