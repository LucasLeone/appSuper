# Django
from django.contrib import admin

# Models
from offers.models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):

    list_display = ('product', 'new_price')
    list_editable = ('new_price',)
    search_fields = ('product',)