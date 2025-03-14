from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm

class OrderListView(ListView):
    model = Order
    template_name = 'orders_app/order_list.html'
    context_object_name = 'orders'
    ordering = ['-order_date']

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders_app/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders_app/order_form.html'
    success_url = reverse_lazy('orders_list') 

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders_app/order_form.html'
    success_url = reverse_lazy('orders_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders_app/order_confirm_delete.html'
    success_url = reverse_lazy('orders_list')
    context_object_name = 'order'