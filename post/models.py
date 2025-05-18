from django.db import models

#Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    description=models.TextField()
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=100)
    images=models.ImageField(upload_to='img')
    date_added=models.DateTimeField(auto_now_add=True)
