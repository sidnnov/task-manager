PORT ?= 8000

# schema-load:
# 	psql page_analyzer < database.sql

# start-postgresql:
# 	sudo service postgresql start

# stop-postgresql:
# 	sudo service postgresql stop

# db-create:
# 	createdb page_analyzer

# db-reset:
# 	dropdb page_analyzer || true
# 	createdb page_analyzer

# connect:
# 	psql -d page_analyzer

install:
	poetry install

build:
	poetry build

dev:
	python manage.py runserver

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager:app

selfcheck:
	poetry check

lint:
	poetry run flake8 task_manager

# pytest:
# 	poetry run pytest

# check: selfcheck pytest lint

# test-coverage:
# 	poetry run pytest --cov=task_manager --cov-report xml