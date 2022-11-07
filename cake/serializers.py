from .models import Cake
from rest_framework import serializers


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['id', 'name', 'description', 'milk_free', 'eggs_free', 'price']
