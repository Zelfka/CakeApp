from django.urls import path
from .views import CakesView, OneCakeView, CakesByOrder

urlpatterns = [
    path('api/cakes/', CakesView.as_view(), name='cakes'),
    path('api/cakes/<str:cake>/', OneCakeView.as_view(), name='one_cake'),
    path('api/cakes/order/<int:order_id>/', CakesByOrder.as_view(), name='cake_order')
]