from rest_framework import serializers 
from product_option.Model.product_option_model import ProductOptionModel 


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionModel
        fields = '__all__'