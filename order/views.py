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
        order = Order.objects.filter(user=request.user).first()
        if order is None:
            return Response({'detail': 'No such order for this user exists'}, status=status.HTTP_400_BAD_REQUEST)

        order.finished = True
        order.date = date
        order.details = details
        order.save()
        return Response({'detail': 'Thank you for you order'}, status=status.HTTP_200_OK)
