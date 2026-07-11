# ShopKart Django Website

ShopKart is a simple Django ecommerce-style homepage inspired by Flipkart. It has a clean shopping layout with a blue top bar, search box, category menu, sale banner, deal highlights, and product cards.

This project is good for learning how Django views, templates, static CSS files, and URL routing work together.

## Preview

Open the home page after starting the server:

```text
http://127.0.0.1:8000/
```

## Features

- Flipkart-style ecommerce homepage
- Sticky blue navigation bar
- Search bar for products and brands
- Category section
- Large sale hero banner
- Top deals product cards
- Featured department banners
- Responsive design for mobile and desktop
- Simple Django template and static CSS setup

## Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite

## Project Structure

```text
.
├── core/
│   ├── settings.py       # Django project settings
│   ├── urls.py           # Main URL routes
│   ├── asgi.py
│   └── wsgi.py
├── home/
│   ├── views.py          # Home page view and page data
│   ├── templates/
│   │   └── home/
│   │       └── home.html # Main website template
│   ├── static/
│   │   └── home/
│   │       └── css/
│   │           └── style.css # Website design
│   ├── models.py
│   ├── admin.py
│   └── tests.py
├── db.sqlite3
├── manage.py
└── README.MD
```

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Django:

```bash
pip install django
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

## Routes

| Route | Page |
| --- | --- |
| `/` | ShopKart home page |
| `/admin/` | Django admin panel |

## Useful Commands

Run Django checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```

## Notes

The current website is a frontend demo. Product names, prices, categories, and offers are added from `home/views.py`. The design is written in `home/static/home/css/style.css`.
