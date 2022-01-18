from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Tshirt(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tshirts_detail', kwargs={'tshirt_id': self.id})
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

class Order(models.Model):
    total_cost= models.DecimalField(max_digits=5, decimal_places=2, default=0)
    date = models.DateField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tshirts = models.ManyToManyField(Tshirt, through='OrderDetail')

class OrderDetail(models.Model):
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
