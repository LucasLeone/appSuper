# Django
from django.db import models

# Models
from products.models import Product


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.name

    def get_price(self):
        return self.product.price_offer if self.product.price_offer else self.product.price

            

class Order(models.Model):
    
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.product.name
    