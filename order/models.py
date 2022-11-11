from django.db import models
from user.models import MyUser
from cake.models import Cake


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateField(null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    details = models.CharField(max_length=500, null=True)
    finished = models.BooleanField(default=False)
    cakes = models.ManyToManyField(Cake)
    sum_cakes = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + '\' order'
