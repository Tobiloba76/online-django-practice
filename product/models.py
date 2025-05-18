from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='img')
    date=models.DateTimeField(auto_now_add=True)
