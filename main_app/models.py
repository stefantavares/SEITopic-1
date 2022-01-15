from django.db import models

# Create your models here.

class Tshirt(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=4, decimal_places=2)
