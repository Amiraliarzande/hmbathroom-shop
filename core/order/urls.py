from django.urls import path
from order.views import OrderListView, OrderHistoryView, CreateOrderView

app_name = 'order'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('history/', OrderHistoryView.as_view(), name='order_history'),
    path('create/', CreateOrderView.as_view(), name='create_order'),
]