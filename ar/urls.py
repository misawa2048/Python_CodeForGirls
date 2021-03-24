from django.urls import path
from . import views

urlpatterns = [
  path('ar', views.index, name='index'),
  path('ar/', views.index, name='index'),
  path('ar/test', views.test, name='test'),
]
