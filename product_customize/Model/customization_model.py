from django.db import models  

from product_customize.Model.options_model import  OptionModel 
from  product_customize.Model.attribute_model import AttributeModel 
from  product.Model.product_model import ProductModel


class ProductCustomizationModel(models.Model):

    attributes= models.ForeignKey(AttributeModel,related_name='attribute_customize',on_delete=models.CASCADE)
    products = models.ForeignKey(ProductModel,related_name='product_customize',on_delete=models.CASCADE)
    options = models.ForeignKey(OptionModel,related_name='option_custom',on_delete=models.CASCADE)

    product_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.attribute.name} - {self.product.name} - {self.option.option_name}'

    