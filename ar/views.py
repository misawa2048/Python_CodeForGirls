from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse
import requests

def index(request):
  return render(request, 'ar/index.html', {})

def test(request):
  return render(request, 'ar/test.html', {})
