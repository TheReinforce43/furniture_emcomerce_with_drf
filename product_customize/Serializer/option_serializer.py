from rest_framework import serializers 


# import related serializer and models 
from product_customize.Model.attribute_model import AttributeModel 
from product_customize.Model.options_model import OptionModel 

from product_customize.Serializer.attribute_serializer import AttributeModelSerializer 



class CreateOptionSerializer(serializers.ModelSerializer): 


    class Meta:
        model = OptionModel
        fields = '__all__'


class GetOptionSerializer(serializers.ModelSerializer):
    attribute = AttributeModelSerializer(read_only=True)

    class Meta:
        model = OptionModel
        fields = '__all__'


# this used for order show flexibility 

class OptionDropdownSerializer(serializers.ModelSerializer):

    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()

    class Meta:
        model = OptionModel
        fields = ('label', 'value')


    def get_label(self, obj):
        return obj.option_name
    
    def get_value(self,obj):
        return obj.pk 

