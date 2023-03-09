from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)