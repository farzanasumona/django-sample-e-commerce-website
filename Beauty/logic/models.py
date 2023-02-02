from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Contact(models.Model):
    username = models.CharField(max_length=100, default='default')
    email = models.CharField(max_length=100)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static')
    price = models.FloatField()
    desc = models.TextField()
    brand = models.ForeignKey(Brand, related_name='products', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, related_name='customers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    total_price = models.FloatField()
    products = models.ManyToManyField(Product, related_name='products', through='OrderProduct')
    is_complete = models.BooleanField(default=False)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='assets', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
















