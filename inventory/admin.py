from django.contrib import admin 
from .models import Product, StockTransaction 



@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin): 
     list_display = ('id', 'name', 'price', 'stock_quantity', 'updated_at') 
     search_fields = ('name',) 


@admin.register(StockTransaction) 
class StockTransactionAdmin(admin.ModelAdmin): 
     list_display = ('id', 'product', 'transaction_type', 'quantity', 'date') 
     list_filter = ('transaction_type',) 
     search_fields = ('product__name',)