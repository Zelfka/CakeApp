from django.urls import path
from .views import CakesView, OneCakeView, ChangeCake

urlpatterns = [
    path('api/cakes/', CakesView.as_view(), name='cakes'),
    path('api/cakes/<int:pk>/', OneCakeView.as_view(), name='one_cake'),
    # path('api/cakes/order/<int:order_id>/', CakesByOrder.as_view(), name='cake_order'),
    path('api/cakes/update/<int:pk>/', ChangeCake.as_view(), name='cake_update')
]