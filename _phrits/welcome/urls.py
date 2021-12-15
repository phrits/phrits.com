from django.urls import re_path, path

from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'(?i)^about/.*$', views.about, name='about'),
]
