from django.urls import path ,include 
from rest_framework.routers import DefaultRouter

from product_option.View.product_api import ProductOptionViewSet 

routers = DefaultRouter() 


routers.register(r'', ProductOptionViewSet, basename='product-option')



urlpatterns = [
    path('',include(routers.urls))
]
