from django.shortcuts import render
from django.utils import timezone
from .models import Rand_int
import requests

def rand_int(request,seed=456):
  rand_int = Rand_int
  return render(request, 'api/rand_int.html', {'rand_int': rand_int, 'seed' : seed })

