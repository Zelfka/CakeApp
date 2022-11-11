import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from user.models import MyUser
from cake.models import Cake
from rest_framework.permissions import IsAuthenticated


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(user=request.user, finished=False).last()
        if order is None:
            return Response({'detail': 'No cakes in the basket'}, status=status.HTTP_400_BAD_REQUEST)
        cakes = order.cakes.all()
        sum = 0
        for cake in cakes:
            sum += cake.price
        order.sum_cakes = order.cakes.count()
        order.total_price = sum
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        cake_id = request.data.get('cake_id')
        cake = Cake.objects.filter(pk=cake_id).first()

        if cake is None:
            return Response({'detail': 'No such cake found.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.filter(user=request.user).last()
        if order is None or order.finished is True:
            order = Order.objects.create(user=request.user)
        order.cakes.add(cake)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        date = request.data.get('date')
        details = request.data.get('details')
        order = Order.objects.filter(user=request.user, finished=False).last()
        if order is None:
            return Response({'detail': 'No such order for this user exists'}, status=status.HTTP_400_BAD_REQUEST)

        order.finished = True
        order.booked_date = date
        order.details = details
        order.save()
        return Response({'detail': 'Thank you for you order'}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        cake = Cake.objects.filter(pk=id).first()
        order = Order.objects.filter(user=request.user, finished=False).last()
        order.cakes.remove(cake)
        return Response(status=status.HTTP_202_ACCEPTED)