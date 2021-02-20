from django.conf import settings
from django.db import models
from django.utils import timezone

class Rand_int(models.Model):
    value = models.IntegerField(default=123)
    seed = 0

    def rand(self):
      self.seed = 456;
      self.value = self.seed*2
      return self.value

    def __str__(self):
        return self.value
