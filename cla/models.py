from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField(upload_to='pics')
    description = models.TextField() 
    price = models.IntegerField()