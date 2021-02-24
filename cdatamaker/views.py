from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
import requests

# Create your views here.
def cdatamaker(request):
  return render(request, 'cdatamaker/index.html', {'cdatamaker': cdatamaker})

def getdata(request):
  r = requests.get("https://news.yahoo.co.jp/")
  return HttpResponse({ 'getdata': r })

