from rest_framework import viewsets
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny 
from rest_framework.views import APIView 
from django.contrib.auth.models import User 
from django.db.models import Sum, F, ExpressionWrapper, DecimalField 
from decimal import Decimal 
from .models import Product, StockTransaction 
from .serializers import ProductSerializer, StockTransactionSerializer
from rest_framework.generics import CreateAPIView 
from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdminUser()]  
        return [IsAuthenticated()]   
    


class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.all().order_by('-date')
    serializer_class = StockTransactionSerializer
    permission_classes = [IsAuthenticated]


# Reports
class CurrentStockAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.all().values('id', 'name', 'stock_quantity', 'price')
        return Response(list(products))


class LowStockAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        threshold = int(request.query_params.get('threshold', 10))
        items = Product.objects.filter(stock_quantity__lt=threshold)
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)


class TotalSalesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_qty = StockTransaction.objects.filter(
            transaction_type=StockTransaction.TRANSACTION_OUT
        ).aggregate(total=Sum('quantity'))['total'] or 0

        expr = ExpressionWrapper(
            F('quantity') * F('product__price'),
            output_field=DecimalField(max_digits=20, decimal_places=2)
        )

        total_value = StockTransaction.objects.filter(
            transaction_type=StockTransaction.TRANSACTION_OUT
        ).aggregate(total=Sum(expr))['total'] or Decimal('0.00')

        return Response({
            'total_quantity_out': total_qty,
            'total_sales_value': str(total_value)
        })
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data): 
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user   


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user_id": user.id,
            "username": user.username,
            "token": token.key
        })




def landing_page(request):
    return HttpResponse("""
        <h1>Inventory & Stock Management</h1>
        <p>Welcome to the Inventory System Backend </p>
        <ul>
            <li><a href='/api/'>Go to API Endpoints</a></li>
            <li><a href='/admin/'>Go to Admin Panel</a></li>
        </ul>
    """)

