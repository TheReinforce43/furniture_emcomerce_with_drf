from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 

routers = DefaultRouter()

from product_customize.View.product_attributes_api import ProductAttributeViewSet
from product_customize.View.attribute_option_api import OptionModelViewSet 
from product_customize.View.product_customize_api import ProductCustomizationViewSet

routers.register(r'product-customize', ProductAttributeViewSet)

routers.register(r'option', OptionModelViewSet)

routers.register(r'productcustomize/attribute', ProductCustomizationViewSet, basename='product-customize-attribute')



urlpatterns = [
    path(r'attribute/',include(routers.urls)),

]


