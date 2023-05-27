### Hexlet tests and linter status:
[![Actions Status](https://github.com/sidnnov/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/sidnnov/python-project-52/actions)
[![My check](https://github.com/sidnnov/python-project-52/actions/workflows/my_check_django.yml/badge.svg)](https://github.com/sidnnov/python-project-52/actions/workflows/my_check_django.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/48472279125a1496186d/maintainability)](https://codeclimate.com/github/sidnnov/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/48472279125a1496186d/test_coverage)](https://codeclimate.com/github/sidnnov/python-project-52/test_coverage)


#### Demonstration:
https://task-manager-project-52.up.railway.app/


## Task manager!
This is a task management application. It helps you organize workflows and distribute tasks among team members.


#### This application is developed with:
- python = "^3.8.1"
- django = "^4.2"
- python-dotenv = "^1.0.0"
- dj-database-url = "^1.3.0"
- gunicorn = "^20.1.0"
- psycopg2-binary = "^2.9.6"
- django-bootstrap4 = "^23.1"
- django-extensions = "^3.2.1"


#### Installation:
-----------------------

Python 3.8+ is required to install task manager. And also need poetry for the assembly of the project.


```
$ git clone git@github.com:sidnnov/python-project-52.git
```
Install dependencies:
```
cd task-manager
make install
```

Create a .env file and specify your database and secret key there.

```
DATABASE_URL = 'YOUR DATABASE'
SECRET_KEY = 'YOUR SECRETKEY'
```
To enable debug mode and include all detailed data on errors, add this variable:
```
DEBUG=True
```

Also, it is necessary to apply all migrations in this project.
```
make migrations
```

Run WSGI server:
```
make start
```

Or you can use django development server:
```
make dev
```
