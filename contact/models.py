from django.db import models
from django.utils import timezone

class contact (models.Model):

    first_name = models.CharField(max_length=50)
    Last_name= models.CharField(max_length=50, blank= True)
    phone= models.CharField(max_length=50)
    email= models.CharField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    decription= models.TextField(blank=True)