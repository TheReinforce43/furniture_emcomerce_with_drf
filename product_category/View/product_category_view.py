from rest_framework.viewsets import ModelViewSet

# import related models and serializers 

from product_category.Model.category_model import ProductCategoryModel 
from product_category.Serializer.category_serializer import (
     ProductCategorySerializer,
     ProductCategoryDropdownSerializer
)    

# import custom permissions 

from support_folder.custom_permission import IsAdminOrGeneralUser 



class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategoryModel.objects.all()
    serializer_class = ProductCategorySerializer 
    permission_classes = [IsAdminOrGeneralUser]  # only admin and general users can perform CRUD operations on this viewset


    def get_queryset(self):
        queryset= self.get_queryset()

        category_name_params = self.request.query_params.get('category_name',None)

        if category_name_params:
            queryset = queryset.filter(category_name__icontains=category_name_params)

        queryset=queryset.order_by('-created_at')

        return queryset
    
    def get_serializer_class(self):
        dropdown_params = self.request.query_params.get('dropdown',None)

        if dropdown_params and  dropdown_params.lower() == 'true':
            return ProductCategoryDropdownSerializer
        
        return self.serializer_class 