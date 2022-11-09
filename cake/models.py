from django.db import models
from order.models import Order


class Cake(models.Model):
    name = models.CharField(max_length=150, unique=True, null=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=300, null=True)
    milk_free = models.BooleanField(default=False)
    eggs_free = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    img = models.CharField(max_length=200, default='fox.ad5cb41c.png')


    def __str__(self):
        return self.name
