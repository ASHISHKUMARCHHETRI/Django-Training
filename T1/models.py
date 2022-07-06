from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    experience=models.IntegerField()
    city=models.CharField(max_length=50)
    def __str__(self):
            return self.name
class Teacher(models.Model):
    name=models.CharField(max_length=50)
    class_assigned=models.CharField(max_length=2)




