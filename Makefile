PORT ?= 8000

migrate:
	poetry run python manage.py makemigrations task_manager
	poetry run python manage.py migrate

# install:
# 	poetry install

# build:
# 	poetry build

dev:
	python manage.py runserver

# start:
# 	gunicorn task_manager.wsgi

# selfcheck:
# 	poetry check

# lint:
# 	poetry run flake8 task_manager

# pytest:
# 	poetry run pytest

# check: selfcheck pytest lint

# test-coverage:
# 	poetry run pytest --cov=task_manager --cov-report xml