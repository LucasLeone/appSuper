# Django
from django.db import models

# Models
from products.models import Product


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.name
        

class Order(models.Model):
    
    item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True)