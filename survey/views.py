from django.shortcuts import render
from .models import Question
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def survey(request):
    return render(request, 'survey.html', {'qs':Question.objects.filter(pk=request.GET["id"]) ,'id':(int(request.GET["id"])+1)})

def result(request):
    return render(request, 'result.html', {})