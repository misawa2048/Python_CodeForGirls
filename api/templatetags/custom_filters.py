#https://docs.djangoproject.com/ja/3.1/howto/custom-template-tags/

from django import template

register = template.Library()

@register.filter()
def f_seed(value,args):
  #from string import split, atoi
  #from myproject.myapp.models import Staff
  return args
  
@register.filter()
def f_times(value,args):
  return value*args
