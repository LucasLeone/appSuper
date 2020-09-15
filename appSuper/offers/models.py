# Django
from django.db import models

# Models
from products.models import Product


class Offer(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    new_price = models.FloatField()