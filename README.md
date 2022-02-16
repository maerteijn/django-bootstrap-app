# django-bootstrap-app
[![Django CI](https://github.com/maerteijn/django-bootstrap-app/actions/workflows/ci.yml/badge.svg)](https://github.com/maerteijn/django-bootstrap-app/actions/workflows/ci.yml)

A clean Poetry based Django app which includes CI

## Install with poetry
```bash
git clone https://github.com/maerteijn/django-bootstrap-app
pip install poetry

# This will also create a virtualenv when not activated
poetry install
```

## Linting
`flake8-black`, `flake8-isort` and `flake8-pylint` are installed too.
```bash
flake8
```

## Black
```bash
black src/
```

## Isort
```bash
isort .
```

## Test
Pytest with coverage is default enabled
```bash
pytest
```

## Run the sandbox
`manage.py` is included in the sandbox for testing the app
```bash
sandbox/manage.py migrate
sandbox/manage.py createsuperuser
sandbox/manage.py runserver
```

