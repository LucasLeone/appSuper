# Django
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView

# Models
from products.models import Product


class ProductsFeed(ListView):
    template_name = 'products/feed.html'
    model = Product
    ordering = ('name')
    context_object_name = 'products'