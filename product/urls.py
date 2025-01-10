from django.urls import path ,include 

from rest_framework.routers import DefaultRouter

from product.View.product_api import ProductViewSet 

routers = DefaultRouter()

routers.register(r'',ProductViewSet,basename='product_view_set')


urlpatterns = [
    path('',include(routers.urls))
]
