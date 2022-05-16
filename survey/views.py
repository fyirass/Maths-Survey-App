from django.shortcuts import render
from .models import Question
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def survey(request):
    return render(request, 'survey.html', {'qs':Question.objects.all()})

def result(request):
    return render(request, 'result.html', {})