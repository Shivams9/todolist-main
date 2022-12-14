
from django.db import models


# Create your models here.
class TodoModel(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    dateoftask = models.DateTimeField()
