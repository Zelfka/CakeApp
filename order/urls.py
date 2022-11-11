from django.urls import path
from .views import OrderView

urlpatterns = [
    path('api/orders/', OrderView.as_view(), name='order'),
    path('api/orders/<int:id>/', OrderView.as_view(), name='order_delete')
]