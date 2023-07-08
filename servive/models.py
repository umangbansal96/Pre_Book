from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    number= models.CharField(max_length=12)
    message= models.TextField()

class Event(models.Model):
    eventname = models.CharField(max_length=122)    
    eventid= models.CharField(max_length=12)
    eventimage = models.CharField(max_length=122)   
    


# Create your models here.
