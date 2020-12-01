# TODO list API
## Auth system

All the requests made to the API need an **Authorization header** with a valid token and the prefix **Bearer**

```Authorization: Bearer <token>```

In order to obtain a valid token it's necesary to send a request `POST /api/v1/auth/token/` with **username** and **password**. To register a new user it's necesary to make a request `POST /api/v1/users/` with the params:
```
username String
password String
confirm_password String
```

## End Points
### Auth
* `POST /api/v1/auth/refresh/`
* `POST /api/v1/auth/token/`

### Users(available for staff users)
* `POST /api/v1/users/`
* `GET /api/v1/users/`
* `PUT /api/v1/users/{username}`
* `GET /api/v1/users/{username}`
* `PATCH /api/v1/users/{username}`
* `DELETE /api/v1/users/{username}`

### Tasks
* `GET /api/v1/tasks/`
* `POST /api/v1/tasks/`
* `PUT /api/v1/tasks/{pk}`
* `GET /api/v1/tasks/{pk}`
* `PATCH /api/v1/tasks/{pk}`
* `DELETE /api/v1/tasks/{pk}`


## Installation

`pip install -r requirements.txt`

## Apply migrations
`python manage.py migrate`

## Create super user
`python manage.py createsuperuser`

## Run the test
`python manage.py test`
