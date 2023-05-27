LOCAL := poetry run python manage.py
PORT ?= 8000

install:
	poetry install

migrations:
	$(LOCAL) makemigrations
	$(LOCAL) migrate

dev:
	$(LOCAL) runserver

start:
	$(LOCAL) migrate
	poetry run gunicorn --bind 0.0.0.0:$(PORT) task_manager.wsgi

lint:
	poetry run flake8 task_manager

test:
	$(LOCAL) test --traceback -v 2

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py

messages:
	poetry run django-admin makemessages -l ru

compilemess:
	poetry run django-admin compilemessages
