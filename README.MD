# Django Core Project

This is a small Django project with a `core` project package and a `home` app. The home page currently returns a simple `Hello, World!` response.

## Project Structure

```text
.
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── home/
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   └── tests.py
├── db.sqlite3
└── manage.py
```

## Requirements

- Python
- Django

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Django:

```bash
pip install django
```

## Run the Project

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the app at:

```text
http://127.0.0.1:8000/
```

## Available Routes

- `/` - Home page returning `Hello, World!`
- `/admin/` - Django admin

## Run Tests

```bash
python manage.py test
```

