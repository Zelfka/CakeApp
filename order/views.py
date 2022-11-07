from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from user.models import MyUser
from cake.models import Cake
from rest_framework.permissions import IsAuthenticated


class OrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        date = request.data.get('date')
        details = request.data.get('details')
        cake_name = request.data.get('cake_name')
        user_id = request.data.get('id')

        user_instance = MyUser.objects.filter(pk=user_id).first()
        cake = Cake.objects.filter(name=cake_name).first()

        if user_instance is None:
            return Response({'detail': 'Wrong user id.'}, status=status.HTTP_400_BAD_REQUEST)

        if cake is None:
            return Response({'detail': 'No such cake found.'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(booked_date=date, details=details, user=user_instance)
        cake.order = order
        cake.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)