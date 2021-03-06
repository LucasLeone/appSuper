# Django
from django import forms

# Models
from products.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'photo']