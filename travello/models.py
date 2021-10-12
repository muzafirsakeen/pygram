from django.db import models
from django.forms import ModelForm


# Create your models here.
class Destination:
    id: int
    name : str
    img : str
    desc : str
    price : int  
    offer = bool
    