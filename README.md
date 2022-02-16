# django-bootstrap-app
[![Django CI](https://github.com/maerteijn/django-bootstrap-app/actions/workflows/ci.yml/badge.svg)](https://github.com/maerteijn/django-bootstrap-app/actions/workflows/ci.yml)

A clean Poetry based Django app which includes CI

## Install with poetry
```bash
git clone https://github.com/maerteijn/django-bootstrap-app
pip install poetry

# This will also create a virtualenv when not activated
poetry install
source $(poetry env info --path)/bin/activate
```

## Linting
`flake8-black`, `flake8-isort` and `flake8-pylint` are installed too.
```bash
flake8
```

## Formatting

### Black
```bash
black src/
```

### Isort
```bash
isort .
```

## Test
Pytest with coverage is default enabled
```bash
pytest
```

## Run the sandbox dev server

When you used a virtualenv yourself (mkvirtualenv or pyenv), you can just run the scripts below.

If not, activate the venv created with poetry:
```bash
source $(poetry env info --path)/bin/activate
```

`manage.py` is included in the sandbox for testing the app
```bash
sandbox/manage.py migrate
sandbox/manage.py createsuperuser
sandbox/manage.py runserver
```