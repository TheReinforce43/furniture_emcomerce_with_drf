from django.db import models 
# from product_option.Model.product_option_model import ProductOptionModel 
from product_category.Model.category_model import ProductCategoryModel



class ProductModel(models.Model):

    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(null=True, blank=True)

    # this is used as base price , further we combine this by product variations 
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # product options are stored in a separate table
    product_category = models.ForeignKey(ProductCategoryModel,related_name='product_category',on_delete=models.CASCADE,null=True)

    
    

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'product :{self.name}'