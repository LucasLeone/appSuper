from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.FloatField()
    price_offer = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='products/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)