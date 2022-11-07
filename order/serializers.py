from .models import Order
from rest_framework import serializers
from user.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['id', 'created', 'booked_date', 'user', 'details']
