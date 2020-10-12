# Django
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

# Models
from products.models import Product
from shopping_cart.models import Order, OrderItem


class AddItem(CreateView):

    model = OrderItem
    template_name = 'shop_cart/add.html'
    success_url = reverse_lazy('shoping_cart:shop')


class ListCart(ListView):

    model = Order
    template_name = 'shop_cart/cart.html'
    # context_object_name = 'products'