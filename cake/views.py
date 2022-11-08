from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cake, PriceList
from .serializers import CakeSerializer, PriceListSerializer
from order.models import Order
from rest_framework.permissions import IsAuthenticated


class CakesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        milk_free = request.data.get('milk_free')
        eggs_free = request.data.get('eggs_free')

        if name is None or description is None:
            return Response({'detail': 'Name and description have to be filled out.'},
                            status=status.HTTP_400_BAD_REQUEST)
        cake = Cake.objects.create(name=name, description=description)
        if milk_free:
            cake.milk_free = milk_free
        if eggs_free:
            cake.eggs_free = eggs_free
        price_list_instance = PriceList.objects.filter().last()
        if price_list_instance is None:
            pass
        else:
            cake_name = name.lower().replace(' ', '_')
            cake.price = price_list_instance.__getattribute__(cake_name)
        cake.save()
        serializer = CakeSerializer(cake)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request):
        cakes = Cake.objects.filter()
        serializer = CakeSerializer(cakes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OneCakeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cake):
        cake_instance = Cake.objects.filter(name=cake).first()
        if cake_instance is None:
            return Response({'detail': 'No such cake found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = CakeSerializer(cake_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CakesByOrder(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order = Order.objects.filter(pk=order_id).first()
        cakes = Cake.objects.filter(order=order)
        serializer = CakeSerializer(cakes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CakePriceList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        price_list_instance = PriceList.objects.filter().last()
        if price_list_instance is None:
            return Response({'detail': 'No pricelist found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PriceListSerializer(price_list_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """ updating one price in price list """
        cake_name = request.data.get('name')
        price = request.data.get('price')

        price_list_instance = PriceList.objects.filter().last()
        if price_list_instance is None:
            return Response({'detail': 'No pricelist found'}, status=status.HTTP_400_BAD_REQUEST)

        price_list_instance.__setattr__(cake_name, price)
        price_list_instance.save()
        serializer = PriceListSerializer(price_list_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ creating new price list """
        price_list_instance = PriceList.objects.create()
        sachr_cake = request.data.get('sachr')
        schwarzwald_cake = request.data.get('schwarzwald')
        chocolate_cake = request.data.get('chocolate')
        vanilla_cake = request.data.get('vanilla')
        fruit_cake = request.data.get('fruit')
        cheesecake = request.data.get('cheesecake')
        carrot_cake = request.data.get('carrot')
        pumpkin_cake = request.data.get('pumpkin')
        price_list_instance.carrot_cake = carrot_cake
        price_list_instance.cheesecake = cheesecake
        price_list_instance.chocolate_cake = chocolate_cake
        price_list_instance.fruit_cake = fruit_cake
        price_list_instance.vanilla_cake = vanilla_cake
        price_list_instance.schwarzwald_cake = schwarzwald_cake
        price_list_instance.pumpkin_cake = pumpkin_cake
        price_list_instance.sachr_cake = sachr_cake
        price_list_instance.save()

        serializer = PriceListSerializer(price_list_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)