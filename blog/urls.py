from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('yahoo', views.yahoo, name='yahoo'),
  #path('forecast', views.forecast, name='forecast'),
]
