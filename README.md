# Validate Password

**Technologies and Tools**

- Python 3.10
- PyTest
- Flask
- Docker

## Running the application

There are two ways to run the application for development: locally through pipenv or through Docker.

### Pipenv mode

To run the application locally, it's necessary to install [pipenv](https://pipenv.pypa.io/en/latest/).

With `pipenv` installed, we can follow the steps below, through terminal.

```terminal
# start the development environment
$ pipenv shell

# install the dependencies
$ pipenv install --system

# run the application
$ flask --app app --debug run --port=8000
```

### Docker mode

To run the application through Docker, we can run the next command, in the terminal:

```terminal
docker compose up --build
```

---

## Tests

To run tests, run the nex command in the terminal:

```terminal
pytest tests.py -v
```

---

## About application

The application has the next routes.:

[POST]

- `/verify`: route to verify the password according to the established rules. The password and rules are sent via JSON in the body of the request. A list is returned with pending issues that the entered password has and a boolean value if it complies with the entered rules.

[Documentation Routes]

- `/apidoc/swagger`: API documentation with Swagger.
- `/apidoc/redoc`: API documentation with Redoc.

---
 