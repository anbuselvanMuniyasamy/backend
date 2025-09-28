from django.db import models 
from django.utils import timezone 
from decimal import Decimal 


class Product(models.Model): 
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True,default="") 
    price = models.DecimalField(max_digits=10, decimal_places=2, 
    default=Decimal('0.00')) 
    stock_quantity = models.PositiveIntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self): 
      return self.name 
    



<<<<<<< HEAD
=======

>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
class StockTransaction(models.Model):
    TRANSACTION_IN = 'IN'
    TRANSACTION_OUT = 'OUT'
    TRANSACTION_CHOICES = [
        (TRANSACTION_IN, 'Stock In'),
        (TRANSACTION_OUT, 'Stock Out'),
    ]

    product = models.ForeignKey(Product, related_name='transactions', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} - {self.quantity}"
