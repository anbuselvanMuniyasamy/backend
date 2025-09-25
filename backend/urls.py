"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import (
    ProductViewSet, StockTransactionViewSet,
    CurrentStockAPIView, LowStockAPIView, TotalSalesAPIView, RegisterAPIView, landing_page
)
from rest_framework.authtoken.views import obtain_auth_token  # <-- token login view

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'transactions', StockTransactionViewSet, basename='transaction')

urlpatterns = [
    path('', landing_page, name='landing'),
    path('admin/', admin.site.urls),

    path('api/auth/register/', RegisterAPIView.as_view(), name='register'),  
    path('api/auth/login/', obtain_auth_token, name='api_token_auth'),       

    
    path('api/reports/current-stock/', CurrentStockAPIView.as_view(), name='current_stock'),
    path('api/reports/low-stock/', LowStockAPIView.as_view(), name='low_stock'),
    path('api/reports/total-sales/', TotalSalesAPIView.as_view(), name='total_sales'),

    path('api/', include(router.urls)),
]


