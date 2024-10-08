from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class Category (models.Model):
    class Meta: 
        verbose_name='Categoria'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
    
class contact (models.Model):

    first_name = models.CharField(max_length=50)
    Last_name= models.CharField(max_length=50, blank= True)
    phone= models.CharField(max_length=50)
    email= models.CharField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    decription= models.TextField(blank=True)
    show= models.BooleanField(default=True)
    picture=  models.ImageField(blank=True, upload_to='picture/%Y/%m/')
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner= models.ForeignKey(User, on_delete= models.SET_NULL, blank=True, null= True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.Last_name}'
    