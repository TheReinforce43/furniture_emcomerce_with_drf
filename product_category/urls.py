from django.urls import path,include 

from rest_framework.routers import DefaultRouter


from product_category.View.product_category_view import ProductCategoryViewSet 


routers = DefaultRouter()

routers.register('product_category', ProductCategoryViewSet)

urlpatterns = [
    path('',include(routers.urls))
]
