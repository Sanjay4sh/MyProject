from django.db import models

from django.db import models

class users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)