from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response="""
<h1>Hello, world!</h1>
"""
    return HttpResponse(response)
