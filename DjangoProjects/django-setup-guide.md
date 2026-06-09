# Django Project Setup (Templates)

Quick guide to start a Django project with templates on Windows, macOS, or Linux.

---

## 1. Create Virtual Environment

**Windows (CMD)**
```cmd
mkdir myproject && cd myproject
python -m venv venv
venv\Scriptsctivate
```

**macOS / Linux (Bash)**
```bash
mkdir myproject && cd myproject
python3 -m venv venv
source venv/bin/activate
```

---

## 2. Install Django

```bash
pip install django
pip freeze > requirements.txt
```

---

## 3. Start Project & App

```bash
django-admin startproject config .
python manage.py startapp pages
```

---

## 4. Folder Structure

```
myproject/
├── config/              # Project settings
│   ├── settings.py
│   └── urls.py
├── pages/               # Your app
│   ├── views.py
│   └── urls.py          # ← Create this
├── templates/           # ← Create this
│   └── pages/           # App HTML files here
├── static/              # ← Create this
│   ├── css/
│   ├── js/
│   └── images/
├── media/               # ← Create this
├── venv/
└── manage.py
```

---

## 5. Configure `config/settings.py`

### Add your app to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',  # ← Add this
]
```

### Set template directory:
```python
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],  # ← Add this
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]
```

### Add static & media settings at the bottom:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## 6. Configure URLs

### Create `pages/urls.py`:
```python
from django.urls import path
# from . import views

app_name = 'pages'

urlpatterns = [
    # path('', views.home, name='home'),
]
```

### Update `config/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # ← Add this
]
```

---

## 7. Create Folders

**Windows (CMD)**
```cmd
mkdir templates\pages
mkdir static\css static\js static\images
mkdir media
```

**macOS / Linux (Bash)**
```bash
mkdir -p templates/pages
mkdir -p static/css static/js static/images
mkdir media
```

---

## 8. Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Quick Commands

| Task | Command |
|------|---------|
| Activate venv (Win) | `venv\Scripts\activate` |
| Activate venv (Mac/Linux) | `source venv/bin/activate` |
| Deactivate venv | `deactivate` |
| Install deps | `pip install -r requirements.txt` |
| Create app | `python manage.py startapp <name>` |
| Make migrations | `python manage.py makemigrations` |
| Apply migrations | `python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Run server | `python manage.py runserver` |

---

## .gitignore

```
venv/
__pycache__/
*.pyc
db.sqlite3
.env
media/
```
