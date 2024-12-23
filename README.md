# FastAPI

FastAPI User Management API
This project is a simple FastAPI-based RESTful API for managing users. It supports basic CRUD operations, including creating, reading, updating, and deleting users. The API is lightweight, making it ideal for learning FastAPI or serving as a foundation for more complex projects.

Features
Retrieve all users: Get a list of all users.
Add a new user: Create a user with unique id, name, and e_mail.
Update a user: Modify the details of an existing user.
Delete a user: Remove a user by their id.

Technologies Used
FastAPI: High-performance API framework.
Pydantic: Data validation and settings management.
Uvicorn: ASGI server for serving the FastAPI application.

Installation
Clone the Repository:
git clone https://github.com/anageguchadze/FastAPI.git

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Run the Application:
uvicorn main:app --reload
This will start the server at http://127.0.0.1:8000.

API Endpoints
Method	Endpoint	Description	Payload Example
GET	/users	Retrieve all users	N/A
POST	/users	Create a new user	{ "id": 0, "name": "name", "e_mail": "test@email.com" }
PUT	/users/{user_id}	Update an existing user by ID	{ "id": 2, "name": "newname", "e_mail": "newmail@gmail.com" }
DELETE	/users/{user_id}	Delete a user by ID	N/A
Example Usage
Create a New User

curl -X 'POST' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "name": "name",
  "e_mail": "test@email.com"
}'

Fetch All Users
curl -X 'GET' \
  'http://127.0.0.1:8000/users' \
  -H 'accept: application/json'

Update a User
curl -X 'PUT' \
  'http://127.0.0.1:8000/users/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "name": "updated_name",
  "e_mail": "updated_email@gmail.com"
}'

Delete a User
curl -X 'DELETE' \
  'http://127.0.0.1:8000/users/2' \
  -H 'accept: application/json'

Requirements
The project uses the following Python packages:
txt
Copy code
annotated-types==0.7.0
anyio==4.7.0
click==8.1.8
colorama==0.4.6
fastapi==0.115.6
h11==0.14.0
idna==3.10
pydantic==2.10.4
pydantic_core==2.27.2
sniffio==1.3.1
starlette==0.41.3
typing_extensions==4.12.2
uvicorn==0.34.0
Install them via:

pip install -r requirements.txt

License
This project is licensed under the MIT License. See the LICENSE file for details.