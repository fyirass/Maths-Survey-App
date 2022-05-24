from django.urls import path
from . import views as views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('survey',views.survey, name = 'survey'),
    path('result',views.result, name = 'result'),
    path('result2',views.result2, name = 'result2'),
]