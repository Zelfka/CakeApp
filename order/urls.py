from django.urls import path
from .views import OrderView, AdminOrdersView

urlpatterns = [
    path('api/orders/', OrderView.as_view(), name='order'),
    path('api/orders/<int:id>/', OrderView.as_view(), name='order_delete'),
    path('api/admin/orders/', AdminOrdersView.as_view(), name='admin_orders'),
    path('api/admin/orders/<int:id>/', AdminOrdersView.as_view(), name='admin_orders_delete')
]