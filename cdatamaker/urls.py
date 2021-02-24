from django.urls import path
from . import views

urlpatterns = [
  path('cdatamaker', views.cdatamaker, name='cdatamaker'),
  path('cdatamaker.getdata', views.getdata, name='getdata'),
]
