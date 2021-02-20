from django.urls import path
from . import views

urlpatterns = [
  path('api', views.rand_int, name='rand_int'),
]
