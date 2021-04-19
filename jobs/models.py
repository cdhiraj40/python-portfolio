from django.db import models

# Create your models here.

"""it essentially it let us create a class Job and
models.Model gives us all sort of background stuff
that allows us to save the object here"""
class Job(models.Model):
    image = models.ImageField(upload_to='images/')#CAN SEARCH DJANGO MODELFIELDS
    summary = models.CharField(max_length=200)#so that all the box looks same in size
