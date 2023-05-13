# API for Yatube v.0.2.0
API services for [Yatube project]
## Features
- User registration
- JWT authentication
- Create or update own Posts
- View Posts
- Become follower of other user

## Tech
- Python 3.9
- Django REST Framework
- JWT


## History
- v.0.2.0 [API_Yatube_final] <- you are here
- v.0.1.0 [API_Yatube] - Create or update own posts. Create comments to posts


## Installation (for Windows)
Clone repository
```sh
git clone git@github.com:KuzenkovAG/api_yatube_final.git
```
Install environment
```sh
cd api_yatube_final/
```
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Scripts/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Make migrate
```sh
python yatube_api/manage.py migrate
```
Run server
```sh
python yatube_api/manage.py runserver
```

## Usage
**Create User / get JWT**
```sh
POST /api/jwt/create/
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
**Receive posts**
```sh
GET /api/v1/posts/

Response:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```


**Create post**
```sh
POST /api/v1/posts/
{
    "text": "string",
    "image": "string",
    "group": 0
}

Response:
{
   "id": 0,
   "author": "string",
   "text": "string",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "string",
   "group": 0
}
```

**Receive post**
```sh
GET /api/v1/posts/{id}/

Response:
{
   "id": 0,
   "author": "string",
   "text": "string",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "string",
   "group": 0
}
```

**Update post**
```sh
PUT /api/v1/posts/{id}/
{
   "text": "string",
   "image": "string",
   "group": 0
}

Response:
{
   "id": 0,
   "author": "string",
   "text": "string",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "string",
   "group": 0
}
```

**Particle update post**
```sh
PATCH /api/v1/posts/{id}/
{
   "text": "string",
   "image": "string",
   "group": 0
}

Response:
{
   "id": 0,
   "author": "string",
   "text": "string",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "string",
   "group": 0
}
```

**Delete post**
```sh
DELETE /api/v1/posts/{id}/
```

**Receive comments**
```sh
GET /api/v1/posts/{post_id}/comments/

Responce
[
   {
      "id": 0,
      "author": "string",
      "text": "string",
      "created": "2019-08-24T14:15:22Z",
      "post": 0
   }
]
```

**Add comment**
```sh
POST /api/v1/posts/{post_id}/comments/
{
   "text": "string"
}

Responce
{
   "id": 0,
   "author": "string",
   "text": "string",
   "created": "2019-08-24T14:15:22Z",
   "post": 0
}
```

**Get comment**
```sh
GET /api/v1/posts/{post_id}/comments/{id}/

Responce
{
   "id": 0,
   "author": "string",
   "text": "string",
   "created": "2019-08-24T14:15:22Z",
   "post": 0
}
```


**Update comment**
```sh
PUT /api/v1/posts/{post_id}/comments/{id}/
{
   "text": "string"
}

Responce
{
   "id": 0,
   "author": "string",
   "text": "string",
   "created": "2019-08-24T14:15:22Z",
   "post": 0
}
```

**Delete comment**
```sh
DELETE /api/v1/posts/{post_id}/comments/{id}/
```


**Get groups**
```sh
GET /api/v1/groups/

[
   {
      "id": 0,
      "title": "string",
      "slug": "string",
      "description": "string"
   }
]
```

**Get group**
```sh
GET /api/v1/groups/{id}/

{
   "id": 0,
   "title": "string",
   "slug": "string",
   "description": "string"
}
```

**Follows**
```sh
GET /api/v1/follow/

Response
[
   {
      "user": "string",
      "following": "string"
   }
]
```

**Follow to user**
```sh
POST /api/v1/follow/
{
   "following": "string"
}


Response
{
   "user": "string",
   "following": "string"
}
```


**Refresh JWT**
```sh
POST /api/v1/jwt/refresh/
{
   "refresh": "string"
}

Response
{
   "access": "string"
}
```

**Check JWT**
```sh
POST /api/v1/jwt/verify/
{
  "token": "string"
}
```


   [Yatube project]: <https://github.com/KuzenkovAG/yatube_new_feature>
   [API_Yatube]: <https://github.com/KuzenkovAG/api_yatube>
   [API_Yatube_final]: <https://github.com/KuzenkovAG/api_yatube_final>
