from django.db import models
import psycopg2

# Create your models here.
class DSB(models.Model):
    NAME: models.CharField(max_length=100)
    IMG : models.ImageField(upload_to='pics')
    desc: models.TimeField()
    price: models.IntegerField()
    offer : models.BooleanField(default=False)
