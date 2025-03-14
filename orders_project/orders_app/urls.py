from django.urls import path
from .views import OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('', OrderListView.as_view(), name='orders_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'), 
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]