from django.db import models

# Create your models here.

class Student(models.Model):
    stdID = models.CharField(max_length = 100)
    stdName = models.CharField(max_length = 100)
    stdCourse = models.CharField(max_length = 100)
    stdYear = models.CharField(max_length = 100)
