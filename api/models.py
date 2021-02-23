from django.conf import settings
from django.db import models

class Rand_int(models.Model):
    value = models.IntegerField(default=12)

    def __str__(self):
        return self.value

    def rand(self,seed=0):
      self.value = seed
      return self.value
