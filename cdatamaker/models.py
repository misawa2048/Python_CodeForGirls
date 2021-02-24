from django.conf import settings
from django.db import models
from django.utils import timezone

class Cdatamaker(models.Model):
    text = models.TextField()

    def combert(self):
      text="?"
      return text

    def __str__(self):
        return self.title
