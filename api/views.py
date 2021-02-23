from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Rand_int
import requests

def usage(request):
  return HttpResponse({'How to use:'})

#https://www.nblog09.com/w/2019/04/07/django-query/
def rand_int(request):
  rand_int = Rand_int
  seed = 1
  if 'seed' in request.GET:
    seed = request.GET['seed']

  return HttpResponse({ m_twice(seed) })
#  return render(request, 'api/rand_int.html', {'rand_int': rand_int, 'seed' : m_twice(seed) })


# may be should move to model.py, but useful like this.
def m_twice(val):
  return int(val)*2


"""
#dummy
def rand(request,seed=1):
  rand_int = Rand_int
  seed=1
  if 'seed' in request.GET:
    seed = request.GET['seed']

  return HttpResponse({rand_int.rand})
"""
