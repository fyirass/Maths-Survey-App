from unicodedata import decimal
from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200, default='I interpret information from a variety of sources to form an opinion about a work/hobby situation.', verbose_name='question')
    domain = models.CharField(max_length=200, default='Data Handling & Chance ', verbose_name='domain')
    affective_zone = models.CharField(max_length=200, default='Manage a Mathematics Containing Situation', verbose_name='affective_zone')
    votes = models.IntegerField(default=0)

    
