from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class DamcoEmployee(models.Model):
    Name=CharField(max_length=50)
    Experiance=IntegerField()
    Location=CharField(max_length=20)

