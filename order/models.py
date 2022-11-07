from django.db import models
from user.models import MyUser


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    booked_date = models.DateField(null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    details = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.user.username + '\' order'