from rest_framework.viewsets import ModelViewSet 

# import related serializer and models 

from product_customize.Model.attribute_model import AttributeModel 
from product_customize.Serializer.attribute_serializer import AttributeModelSerializer

from support_folder.custom_permission import IsAdminOrGeneralUser


class ProductAttributeViewSet(ModelViewSet):
    queryset = AttributeModel.objects.all()
    serializer_class = AttributeModelSerializer
    permission_classes=[IsAdminOrGeneralUser]