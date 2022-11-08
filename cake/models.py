from django.db import models
from order.models import Order


class Cake(models.Model):
    name = models.CharField(max_length=150, unique=True, null=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=300, null=True)
    milk_free = models.BooleanField(default=False)
    eggs_free = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name


class PriceList(models.Model):
    sachr_cake = models.IntegerField(default=0)
    schwarzwald_cake = models.IntegerField(default=0)
    chocolate_cake = models.IntegerField(default=0)
    vanilla_cake = models.IntegerField(default=0)
    fruit_cake = models.IntegerField(default=0)
    cheesecake = models.IntegerField(default=0)
    carrot_cake = models.IntegerField(default=0)
    pumpkin_cake = models.IntegerField(default=0)

    def __str__(self):
        return f'Price list with id {self.pk}'