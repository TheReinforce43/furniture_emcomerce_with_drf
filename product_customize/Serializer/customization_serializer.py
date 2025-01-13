from rest_framework import serializers 


# import related serializer 
from product_customize.Model.customization_model import ProductCustomizationModel 

from product_customize.Serializer.attribute_serializer import AttributeModelSerializer 
from product_customize.Serializer.option_serializer import GetOptionSerializer 
from product.Serializer.product_serializer import GetProductSerializer  

class create_product_customize_serializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCustomizationModel
        fields = '__all__'




# Get serializer 

class Get_product_customize_serializer(serializers.ModelSerializer):
    products = GetProductSerializer(read_only=True)
    attributes = AttributeModelSerializer( read_only=True)
    options = GetOptionSerializer( read_only=True)

    class Meta:
        model = ProductCustomizationModel
        fields = '__all__'



class product_customize_price_dropdown_serializer(serializers.ModelSerializer):

    label= serializers.SerializerMethodField()
    value= serializers.SerializerMethodField()

    class Meta:
        model = ProductCustomizationModel
        fields = ['label', 'value']


    def get_label(self, obj):
        return obj.product_price
    
    def get_value(self, obj):
        return obj.pk

    

    
