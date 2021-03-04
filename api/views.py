from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse
import requests
from .models import Rand_int
from .models import TextToWav

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
  t2w = TextToWav
  t2w.volume=0.2
  filepath = "output"
  fullfilepath = t2w.get_full_path(t2w)+"output"
  #t2w = TextToWav(samplerate=16000, volume=0.5)
  t2w.text_to_wav(t2w,_text=text,_filename=filepath)
  text = t2w.cat_text2(t2w,_text=text)
  text = text+"!"
  return HttpResponse('{"text":'+'"{0}"'.format(text)+',"path":"'+filepath+'","fullpath":"'+fullfilepath+'"}');
  #return HttpResponse('{"text":'+'"{0}"'.format(text+'--'+text)+'}');


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
