from rest_framework import serializers 
from product_customize.Model.attribute_model import AttributeModel 


class AttributeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeModel
        fields = '__all__'