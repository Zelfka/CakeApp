from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from cake.models import Cake
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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


class AdminOrdersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.filter()
        if len(orders) == 0:
            return Response({'detail': 'No orders found'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        date = request.data.get('date')
        name = request.data.get('name')
        username = request.data.get('username')
        state = request.data.get('order_state')
        orders = Order.objects.filter()
        orders_resp = []

        if username:
            for order in orders:
                if username in order.user.username:
                    orders_resp.append(order)
            if len(orders_resp) == 0:
                return Response({'detail': 'No orders with this username exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if date:
            for order in orders:
                if str(order.booked_date) == date:
                    orders_resp.append(order)
            if len(orders_resp) == 0:
                return Response({'detail': 'No orders for this date.'}, status=status.HTTP_400_BAD_REQUEST)

        if name:
            for order in orders:
                for cake in order.cakes.all():
                    if name in cake.name:
                        orders_resp.append(order)
            if len(orders_resp) == 0:
                return Response({'detail': 'No orders with this cake exist.'}, status=status.HTTP_400_BAD_REQUEST)
        if state:
            for order in orders:
                if order.state == state:
                    orders_resp.append(order)

        if len(orders_resp) == 0:
            return Response({'detail': 'No orders with these details exist.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = OrderSerializer(orders_resp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        id = request.data.get('order_id')
        order = Order.objects.filter(pk=id).first()
        if order is None:
            return Response({'detail': 'No such order exists'}, status=status.HTTP_400_BAD_REQUEST)
        order.state = 'Closed'
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        order = Order.objects.filter(pk=id).first()
        if order is None:
            return Response({'detail': 'No such order exists'}, status=status.HTTP_400_BAD_REQUEST)
        order.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
