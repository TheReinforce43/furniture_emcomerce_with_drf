from rest_framework import serializers 


# import related serializer and models 
from product.Model.product_model import ProductModel 
from product_category.Serializer.category_serializer import ProductCategoryDropdownSerializer


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'



# this serializer used for get 

class GetProductSerializer(serializers.ModelSerializer):

    product_category=ProductCategoryDropdownSerializer(read_only=True,many=False)

    class Meta:
        model = ProductModel
        fields = '__all__'