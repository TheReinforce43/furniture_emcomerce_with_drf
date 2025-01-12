from rest_framework.viewsets import ModelViewSet 


# import related serializer and models 

from product_customize.Model.options_model import OptionModel 

from  product_customize.Serializer.option_serializer import (
    CreateOptionSerializer,
    GetOptionSerializer,
    OptionDropdownSerializer 
)

# import custom permissions 

from support_folder.custom_permission import IsAdminOrGeneralUser 


class OptionModelViewSet(ModelViewSet):

    queryset = OptionModel.objects.all()
    serializer_class = GetOptionSerializer
    permission_classes = [IsAdminOrGeneralUser]


    def get_queryset(self):
        queryset = super().get_queryset()

        option_name_params = self.request.query_params.get('option_name', None)
        attribute_params = self.request.query_params.get('attribute_id', None)  


        if option_name_params:
            queryset = queryset.filter(option_name__icontains=option_name_params)

        if attribute_params:
            queryset = queryset.filter(attribute__id=attribute_params)

        queryset =  queryset.order_by('-created_at')

        return queryset
    

    def get_serializer_class(self):
        
        dropdown_params = self.request.query_params.get('dropdown',None)
        if dropdown_params and dropdown_params.lower()=='true':

            return OptionDropdownSerializer
        
        return self.serializer_class







