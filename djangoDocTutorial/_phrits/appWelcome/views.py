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
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

# **** Tutorial
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'appWelcome/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request, 'appWelcome/detail.html', {'question': question})
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    # Alternative idiom
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'appWelcome/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

