from django.db import models
from django.contrib.auth.models import User

class Good(models.Model):
    category = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    imagelink = models.ImageField(upload_to='uploads/', default='', blank=True, null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.material + " " + self.name

class Stock(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantityInStock = models.IntegerField(default=0)
    container = models.CharField(max_length=20, default='box')

class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gold_quantity = models.IntegerField(default=0)

# Create your models here.
