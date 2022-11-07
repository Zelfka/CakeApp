from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cake
from .serializers import CakeSerializer
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