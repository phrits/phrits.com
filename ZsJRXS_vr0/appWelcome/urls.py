# .../app/views.py
# May need to be created or copied from parent folder.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
