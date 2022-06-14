
from multiprocessing import context
from django.shortcuts import render, redirect
from requests import request
from .models import Question
from django.db.models import Max
# Create your views here.



def index(request ):
    return render(request, 'index.html', {})



def survey(request):
    
    Id = int(request.GET["id"])
    
    vote = request.POST.get('radio')
    
    if vote==None : 
        Question.objects.filter(id = Id-1).update(votes = 0)
    else :
        Question.objects.filter(id = Id-1).update(votes = vote)
    
    if Id == 33 :
        return redirect('result')

    
    return render(request, 'survey.html', {'qs': Question.objects.filter(pk=request.GET["id"]), 'id':(Id+1)})
    


def result(request):
    
    d_data = Question.objects.filter(domain = "Data Handling & Chance").aggregate(Max('votes'))
    dm_data = d_data.get('votes__max')

    d_space = Question.objects.filter(domain = "Space & Shape").aggregate(Max('votes'))
    dm_space = d_space.get('votes__max')

    d_pattern = Question.objects.filter(domain = "Pattern & Relationship").aggregate(Max('votes'))
    dm_pattern = d_pattern.get('votes__max')

    d_quantity = Question.objects.filter(domain = "Quantity & Number").aggregate(Max('votes'))
    dm_quantity = d_quantity.get('votes__max')


    a_manage = Question.objects.filter(affective_zone = "Manage a Mathematics Containing Situation").aggregate(Max('votes'))
    am_manage = a_manage.get('votes__max')

    a_problem = Question.objects.filter(affective_zone = "Problem Solve").aggregate(Max('votes'))
    am_problem = a_problem.get('votes__max')

    
    return render(request, 'result.html', {'dm_data': dm_data,'dm_space': dm_space, 'dm_pattern' : dm_pattern, 'dm_quantity' : dm_quantity, 'am_manage': am_manage , 'am_problem': am_problem })



def result2(request):

    a_manage = Question.objects.filter(affective_zone = "Manage a Mathematics Containing Situation").aggregate(Max('votes'))
    am_manage = a_manage.get('votes__max')

    a_problem = Question.objects.filter(affective_zone = "Problem Solve").aggregate(Max('votes'))
    am_problem = a_problem.get('votes__max')



    return render(request, 'result2.html', {'am_manage': am_manage , 'am_problem': am_problem })
