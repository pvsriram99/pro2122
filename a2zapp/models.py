from django.db import models

# Create your models here.
class empmodel(models.Model):
    EmpName = models.CharField(max_length=75)
    EmpId = models.IntegerField()
    Designation = models.CharField(max_length=50)
    Dateofjoin = models.CharField(max_length=15)
    Department = models.CharField(max_length=75)
    Salary = models.IntegerField()
    Experience = models.CharField(max_length=50)
class news(models.Model):
    occation = models.TextField()

class calender(models.Model):
    Date = models.CharField(max_length=15)
    Occation = models.TextField()