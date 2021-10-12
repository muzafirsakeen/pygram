
from django.db import models


  
# Create your models here.
class Destination(models.Model):
    NAME: models.CharField(max_length=100)
    EMAIL : models.CharField(max_length=255)
    PASSWORD: models.CharField(max_length=100)

class cars(models.Model):
    name = models.TextField()

    license = models.TextField()
    
class bank(models.Model):
    name = models.TextField()

    email = models.TextField()
    phone = models.TextField()

    password = models.TextField()
    
    
class Userinfo(models.Model):

    name                    = models.CharField(max_length=100)
    blood_group             = models.CharField(max_length=10)
    phone_number            = models.TextField(max_length=10)
    email                    = models.CharField(max_length=50)