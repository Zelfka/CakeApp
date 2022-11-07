from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    zip_code = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.username



