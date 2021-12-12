# phrits.com

## DJango Notes

### First Steps.

1. Make sure it's installed.
1. Install the project from project's root.
1. Install an Application
1. Create the database structure, etc.
1. Start the django webservice.


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
- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial>`python manage.py runserver`

##### Checkpoint: http://localhost:8000 shows the Django welcome screen.

- (django) E:\Dropbox\Active\phrits.com\dJangoDocTutorial>`python manage.py startapp appWelcome`
```
# /phrits/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('appWelcome.urls')),
    path('admin/', admin.site.urls),
```

```
# /appWelcome/urls.py
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

```
# /appWelcome/views.py
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, world!</h1>')
```

##### Checkpoint: Hello, world!
