from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    esal=models.IntegerField()
    ecity=models.CharField(max_length=20)
