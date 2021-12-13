"""
Templates:  from django.shortcuts import render
Send:       from django.http import HttpResponse

Default home page for appWelcome.

It's also the home page for the site.
    _phrits/urls.file calls:
        path('', include('appWelcome.urls')),
in its urlpatterns.

def index(request):
    return HttpResponse("You're at the appWelcome index.")
"""
from django.shortcuts import render
from django.http import HttpResponse

# **** Tutorial
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

