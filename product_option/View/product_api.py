from rest_framework.viewsets import ModelViewSet
from product_option.Model.product_option_model import ProductOptionModel 
from product_option.Serializer.product_serializer import ProductOptionSerializer 

from rest_framework.permissions import IsAuthenticated,IsAdminUser 
from support_folder.custom_permission import IsAdminOrGeneralUser




class ProductOptionViewSet(ModelViewSet):
    queryset = ProductOptionModel.objects.all()
    serializer_class = ProductOptionSerializer  # Serializer for ProductOptionModel

    # apply has object custom permissions here  
    # if admin, can access ,
    # otherwise can only view 

    permission_classes=[IsAdminOrGeneralUser]

    def get_queryset(self):
        queryset = super().get_queryset()


        option_name=self.request.query_params.get('option_name',None)
        

        # here apply params 
        if option_name:
            queryset = queryset.filter(option_name__icontains=option_name)

        return queryset
                                                





