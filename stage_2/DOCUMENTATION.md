# API Documentation for Simple Person Management API

## Introduction
This API provides basic CRUD operations for a person. It has the following endpoints:
  - Adding a new person.  =>/api
  - Fetching details of a person.  => /api/user_id
  - Modifying details of an existing person => /api/user_id
  - Removing a person => /api/user_id
### API Overview
- **Description**: This API allows you to manage information about people, including creating, reading, updating, and deleting person records.
- **Base URL**: `http://hng.flanders.tech/api`

{user_id} 
## Endpoints
### Create a New Person

- **Endpoint**: `POST /api`
- **Description**: Create a new person record.
- **Request Body**:
  - Form data or JSON object containing person details:
    - `name` (string, required): The name of the person.

#### Example Request
```http
POST /api
Content-Type: application/json

{
  "name": "Luna Lovegood",
}
```

#### Example Response
```json
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "Luna Lovegood",
}
```

### Retrieve Person Details

- **Endpoint**: `GET /api/{user_id}`
- **Description**: Fetch details of a specific person by their `user_id`.
- **URL Parameters**:
  - `user_id` (integer, required): The unique identifier of the person.

#### Example Request
```http
GET /api/1
```

#### Example Response
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Luna Lovegood",
}
```

### Update Person Details

- **Endpoint**: `PUT /api/{user_id}`
- **Description**: Update the details of an existing person by their `user_id`.
- **URL Parameters**:
  - `user_id` (integer, required): The unique identifier of the person.
- **Request Body**:
  - Form data or JSON object containing person details to update:
    - `name` (string, optional): The updated name of the person.

#### Example Request
```http
PUT /api/1
Content-Type: application/json

{
  "name": "Horace Slughorn"
}
```

#### Example Response
```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Horace Slughorn",
}
```

### Delete a Person

- **Endpoint**: `DELETE /api/{user_id}`
- **Description**: Remove a person by their `user_id`.
- **URL Parameters**:
  - `user_id` (integer, required): The unique identifier of the person.

#### Example Request
```http
DELETE /api/1
```

#### Example Response
```json
HTTP/1.1 204 No Content
```

## Error Handling

### Create a Person
The field should be only be a string. Integers or any other data type are not allowed.
#### Example Request
```http
POST /api
Content-Type: application/json

{
  "name": 20,
}

```
#### Example Response 
```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{"Invalid data: Expecting a string"}
```

### Retrieve a person's details
When the requested user_id is not present in the database.
#### Example Request
```http
GET /api/1
```
#### Example Response 
```json
HTTP/1.1 404 Not Found
Content-Type: application/json

{"Error: User {user_id} not found"}
```

### Update a person's details
When the requested user_id is not present in the database.
#### Example Request
```http
GET /api/1
```
#### Example Response 
```json
HTTP/1.1 404 Not Found
Content-Type: application/json

{"Error: User {user_id} not found"}
```

### Delete a Person
When the requested user_id is not present in the database.
#### Example Request
```http
GET /api/1
```
#### Example Response 
```json
HTTP/1.1 404 Not Found
Content-Type: application/json

{"Error: User {user_id} not found"}
```
