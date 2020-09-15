# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Forms
from products.forms import ProductForm

# Models
from products.models import Product


class ProductsFeed(ListView):
    template_name = 'products/feed.html'
    model = Product
    ordering = ('-created')
    context_object_name = 'products'


class CreateProduct(CreateView):
    template_name = 'products/create.html'
    form_class = ProductForm
    success_url = reverse_lazy("products:feed")


def searchProduct(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query)
        )
        results = Product.objects.filter(qset)
    else:
        results = []
    return render(None, 'products/search.html', {
        "results": results,
        "query": query
    })