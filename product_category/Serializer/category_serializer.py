from rest_framework import serializers 


from product_category.Model.category_model import ProductCategoryModel 



class ProductCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = ProductCategoryModel
        fields =['category_name','description']



# create category serializer for dropdown serializer 

class ProductCategoryDropdownSerializer(serializers.ModelSerializer):

    label = serializers.SerializerMethodField()
    value = serializers.SerializerMethodField()


    class Meta:
        model = ProductCategoryModel
        fields = ['label', 'value']

    def get_label(self, obj):
        return obj.category_name
    
    def get_value(self, obj):
        return obj.pk