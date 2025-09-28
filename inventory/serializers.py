from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Product, StockTransaction 



class UserSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = User 
    fields = ('id', 'username', 'email') 

 
class ProductSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Product 
    fields = ('id', 'name', 'description', 'price', 'stock_quantity','created_at', 'updated_at') 
    read_only_fields = ('created_at', 'updated_at') 



class StockTransactionSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = StockTransaction
        fields = ('id', 'product', 'product_name', 'quantity', 'transaction_type', 'date', 'note')
        read_only_fields = ('date',)

    def validate(self, data):
        product = data.get('product')
        if not product:
            raise serializers.ValidationError("Product is required.")

        qty = data.get('quantity')
        type = data.get('transaction_type')

        if qty is None or qty <= 0:
            raise serializers.ValidationError("Quantity must be positive.")

        if type == StockTransaction.TRANSACTION_OUT:
            if product.stock_quantity < qty:
                raise serializers.ValidationError("Not enough stock for this transaction.")

        return data

    def create(self, validated_data):
        product = validated_data['product']
        qty = validated_data['quantity']
        type = validated_data['transaction_type']

        if type == StockTransaction.TRANSACTION_IN:
            product.stock_quantity += qty
        else:
            product.stock_quantity -= qty
        product.save()

        return StockTransaction.objects.create(**validated_data)