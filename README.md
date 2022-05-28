# Django REST Framework / Docker /PSQL

## **Author: Ammar Abul-Feilat**

## overview

Use Django REST Framework to create an API, then “containerize” it with Docker. +PSQL

## Architecture

- Python 3.9.5
- Django 4.0.4
- Docker 20.10.12
- PostgreSQL 11

## Run the Project

Open Console in Main Project Directory.

```md
python manage.py runserver

username = admin
password = 0000

check carefully the links in the browser

docker-compose up

you can run docker on localhost:8000  
or 127.0.0.0:8000

python manage.py test
```
