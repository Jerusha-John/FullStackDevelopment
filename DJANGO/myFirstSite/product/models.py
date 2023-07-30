from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2550)

class offers(models.Model):
    ItemName = models.CharField(max_length=255)
    ItemPrice = models.FloatField()
    ItemStock = models.IntegerField()
    ItemImage = models.CharField(max_length=2550)        