from rest_framework.viewsets import ModelViewSet 

# import related serializers and models 

from product.Model.product_model import ProductModel 


from product.Serializer.product_serializer import (
    CreateProductSerializer,
    GetProductSerializer 
)

from support_folder.custom_permission import IsAdminOrGeneralUser


class ProductViewSet(ModelViewSet):

    queryset = ProductModel.objects.all()

    # permission_classes = [IsAdminOrGeneralUser]

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CreateProductSerializer
        return GetProductSerializer 
    
    def get_queryset(self):
        
        queryset = super().get_queryset()

        category_params = self.request.query_params.get('product_category',None)

        if category_params:
            queryset = queryset.filter(product_category=category_params)

        queryset = queryset.order_by('-created_at')

        return queryset 


