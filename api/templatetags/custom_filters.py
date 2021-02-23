#https://docs.djangoproject.com/ja/3.1/howto/custom-template-tags/

from django import template

register = template.Library()

@register.filter(base_num=123)
def times_two(value):
  #from string import split, atoi
  #from myproject.myapp.models import Staff
  return value*2

