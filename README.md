# Yatube API

Provide API services for:
- Create User
- Create Posts
- View Posts of other Users
- Become follower of other user

## Tech
- Python 3.9
- Django REST Framework
- JWT autentification


## Installation (for Windows)
1. Clone repository on your PC
2. Open terminal and install vertual enviroment
```sh
py -3.9 -m venv venv
```
3. Install requirements
```sh
pip install -r requirements.txt
```
4. Make migrations and run server
```sh
python manage.py migrate
python manage.py runserver
```

## Usage
Receive all ENDPOINST
/redoc/

## Example of requests
Create User
```sh
GET /api/jwt/create/
Payload:
{
    "username": "string",
    "password": "string"
}

Response:
{
    "refresh": "string",
    "access": "string"
}
```
Receive posts
```sh
GET /api/v1/posts/
```
Create post
```sh
POST /api/v1/posts/
Payload:
{
    "text": "string",
    "image": "string",
    "group": 0
}
```