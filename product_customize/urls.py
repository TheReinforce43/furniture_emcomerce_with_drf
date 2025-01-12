from django.urls import path ,include 
from rest_framework.routers import DefaultRouter 

routers = DefaultRouter()

from product_customize.View.product_customize_api import ProductCustomizeViewSet
from product_customize.View.attribute_option_api import OptionModelViewSet 

routers.register(r'product-customize', ProductCustomizeViewSet)

routers.register(r'option', OptionModelViewSet)



urlpatterns = [
    path(r'attribute/',include(routers.urls)),

]


