from rest_framework.viewsets import ModelViewSet 

# import related serializer and models 

from product_customize.Model.customization_model import ProductCustomizationModel 
from product_customize.Serializer.customization_serializer import (
    create_product_customize_serializer,
    Get_product_customize_serializer,
    product_customize_price_dropdown_serializer 
)

# import custom permissions 
from support_folder.custom_permission import IsAdminOrGeneralUser 



class ProductCustomizationViewSet(ModelViewSet):

    queryset = ProductCustomizationModel.objects.all()
    permission_classes = [IsAdminOrGeneralUser]


    def get_serializer_class(self):

        dropdown_params = self.request.query_params.get('dropdown', None)

        if dropdown_params and dropdown_params.lower() == 'true':
            return product_customize_price_dropdown_serializer

        if self.action in ['create', 'update', 'partial_update']:
            return create_product_customize_serializer

        return Get_product_customize_serializer
    

    def get_queryset(self):
        queryset = super().get_queryset()

        attributes_params = self.request.query_params.get('attribute_id',None)
        option_params = self.request.query_params.get('option_id',None)
        products_params = self.request.query_params.get('product_id',None)

        if attributes_params:
            queryset = queryset.filter(attributes__id=attributes_params)

        if option_params:
            queryset = queryset.filter(options__id=option_params)
        
        if products_params:
            queryset = queryset.filter(products__id=products_params)

        queryset =  queryset.order_by('-created_at')

        return queryset  
    
 