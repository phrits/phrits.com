# phrits.com

## DJango Notes

### First Steps.

1. Make sure it's installed.
1. Install the project from project's root.
1. Install an Application
1. Create the database structure, etc. (migrate)
1. Create models.
1. Create migrations for those changes.
1. Apply those changes to the database. (migrate)
1. Create admin account
1. Make models available for djangoAdmin access. GUI data edits.

### Useful Knowledge
```
# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>
```

## History

### Branch creatingSimpleWDjango-0924-ZsJRXS_vrw0 

2021-12-11

- *Make sure it's installed.*
(django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>`python -m django --version`

- *Install the project from project's root.*
(django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>`django-admin startproject phrits`
    - Note: All the files in `.\phrits\phrits` were promoted a level

- *Install an Application*
(django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>`python manage.py startapp appWelcome`

- *Create the database structure, etc.*
(django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>`python manage.py migrate`

- *Start the django webservice*
(django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>`python manage.py runserver`

##### Checkpoint: http://localhost:8000 shows the Django welcome screen.

### Branch djangoDocTutorial

2021-12-11

- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial>`python -m django --version`
- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial>`django-admin startproject phrits`
- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial\_phrits>`python manage.py runserver`

##### Checkpoint: http://localhost:8000 shows the Django welcome screen.

- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial>`python manage.py startapp appWelcome`

- `/_phrits/urls.py`
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('appWelcome.urls')),
    path('admin/', admin.site.urls),
```

- `/_phrits/appWelcome/urls.py`
```
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- `/_phrits/appWelcome/views.py`
```
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')
```

##### Checkpoint: Hello, world!


- *Create the database, etc.* (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial\_phrits>`python manage.py migrate`

- `_phrits/appWelcome/apps.py`
```
from django.apps import AppConfig


class AppwelcomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appWelcome'
```

- `/_phrits/appWelcome/models.py`
```from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
- `/_phrits/settings.py
```
INSTALLED_APPS = [
    'appWelcome.apps.AppwelcomeConfig',
]
```

##### Checkpoint: Models created

- *View in SQL (Optional)* (django) E:\Dropbox\Active\phrits.com\djangoDocTutorial\_phrits>`python manage.py sqlmigrate appWelcome 0001`

- *Make the database changes.* (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial\_phrits>`python manage.py migrate`

> three-step guide to making model changes:
2. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
2. Run python manage.py migrate to apply those changes to the database.

##### Checkpoint: Database schema changes implemented

- *Create Django admin account.* (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial\_phrits>`python manage.py createsuperuser`

- `_phrits/appWelcome/admin.py` (Probably optional.)
```
polls/admin.py¶
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
