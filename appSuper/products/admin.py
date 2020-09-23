# Django
from django.contrib import admin

# Models
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'price_offer', 'photo')
    list_editable = ('name', 'price', 'price_offer', 'photo')
    search_fields = ('name',)
    list_filter = ('created', 'modified')