from .models import Cake, PriceList
from rest_framework import serializers


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ['id', 'name', 'description', 'milk_free', 'eggs_free', 'price']


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ['id', 'sachr_cake','schwarzwald_cake', 'chocolate_cake',
                  'vanilla_cake', 'fruit_cake', 'cheesecake', 'carrot_cake', 'pumpkin_cake']