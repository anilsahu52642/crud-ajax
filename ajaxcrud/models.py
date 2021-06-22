from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=64)
    roll=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=64)