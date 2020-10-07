# Django
from django.contrib import admin

# Models
from shopping_cart.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list = ('item')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = ('product', 'quantity')