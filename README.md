# Creating a simple website with the Django framework

URL: https://www.youtube.com/watch?v=ZsJRXS_vrw0

Accessed ca. 2021-12-11

## DJango Notes

- (django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>django-admin startproject phrits
    - Note: All the files in .\phrits\phrits were promoted a level
- (django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>python manage.py startapp appWelcome  
- (django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>python manage.py migrate
- (django) E:\Dropbox\Active\phrits.com\ZsJRXS_vr0>python manage.py runserver

Checkpoint: http://localhost:800 shows the Django welcome screen.

- ```# .../app/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")```


## Source Notes
IDG TECHtalk
47.2K subscribers

Django is among Python's most popular web framework packages. Here's how to get up and running with a simple project.

Official Django site: https://djangoproject.com/

Follow TECH(talk) for the latest tech news and discussion!
------------------------------­----
SUBSCRIBE: http://www.youtube.com/subscription_c...

FACEBOOK: https://www.facebook.com/idgtechtalk/

TWITTER: https://twitter.com/IDGTechTalk

IDG ENTERPRISE WEBSITES 

Computerworld: https://www.computerworld.com/video/s...

CIO: https://www.cio.com/video/series/8534...

CSO: https://www.csoonline.com/video/serie...

InfoWorld: https://www.infoworld.com/video/serie...

Network World: https://www.networkworld.com/video/se...

