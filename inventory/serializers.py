from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Product, StockTransaction 
<<<<<<< HEAD



=======
from decimal import Decimal 


      #  user serializer (for registration response) 
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
class UserSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = User 
    fields = ('id', 'username', 'email') 

 
<<<<<<< HEAD
=======
           # product 
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
class ProductSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Product 
    fields = ('id', 'name', 'description', 'price', 'stock_quantity','created_at', 'updated_at') 
    read_only_fields = ('created_at', 'updated_at') 


<<<<<<< HEAD

=======
         # stock transaction 
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
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
<<<<<<< HEAD
        type = data.get('transaction_type')
=======
        ttype = data.get('transaction_type')
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46

        if qty is None or qty <= 0:
            raise serializers.ValidationError("Quantity must be positive.")

<<<<<<< HEAD
        if type == StockTransaction.TRANSACTION_OUT:
=======
        if ttype == StockTransaction.TRANSACTION_OUT:
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
            if product.stock_quantity < qty:
                raise serializers.ValidationError("Not enough stock for this transaction.")

        return data

    def create(self, validated_data):
        product = validated_data['product']
        qty = validated_data['quantity']
<<<<<<< HEAD
        type = validated_data['transaction_type']

        if type == StockTransaction.TRANSACTION_IN:
=======
        ttype = validated_data['transaction_type']

        if ttype == StockTransaction.TRANSACTION_IN:
>>>>>>> 0058cfcddd355e69c1d8cea8f79bf7aa2579ae46
            product.stock_quantity += qty
        else:
            product.stock_quantity -= qty
        product.save()

        return StockTransaction.objects.create(**validated_data)