from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Rand_int
from django.urls import reverse
import requests

def usage(request):
  #return HttpResponse({'How to use api/:<br>/rand_int?seed=[num]<br>/t2a?text=[text]<br>/s2a/[text]<br>'})
  return render(request, 'api/usage.html', {})

#https://www.nblog09.com/w/2019/04/07/django-query/
def rand_int(request):
  rand_int = Rand_int
  seed = 1
  if 'seed' in request.GET:
    seed = request.GET['seed']

  return HttpResponse({ m_twice(seed) })
#  return render(request, 'api/rand_int', {'rand_int': rand_int, 'seed' : m_twice(seed) })

def t2a(request):
  text='"no data"'
  if 'text' in request.GET:
    text = request.GET['text']
  return HttpResponse({ text_to_audio(text) })

def s2a(request,text):
  return HttpResponse("[{'text':"+'{0}'.format(text)+"}]")


# may be should move to model.py, but useful like this.
def m_twice(val):
  return int(val)*2

def text_to_audio(text):
  return "{'text':"+text+"}"


"""
#dummy
def rand(request,seed=1):
  rand_int = Rand_int
  seed=1
  if 'seed' in request.GET:
    seed = request.GET['seed']

  return HttpResponse({rand_int.rand})
"""
