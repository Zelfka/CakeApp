from .models import Order
from rest_framework import serializers
from user.serializers import UserSerializer
from cake.serializers import CakeSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cakes = CakeSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created', 'booked_date', 'user', 'details', 'finished', 'cakes', 'sum_cakes', 'total_price']
