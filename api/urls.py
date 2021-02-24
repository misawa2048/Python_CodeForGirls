from django.urls import path
from . import views

urlpatterns = [
  path('api', views.usage, name='usage'),
  path('api/rand_int', views.rand_int, name='rand_int'),
  path('api/t2a', views.t2a, name='t2a'),
]
