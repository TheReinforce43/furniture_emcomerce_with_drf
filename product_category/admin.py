from django.contrib import admin

# Register your models here.
from product_category.Model.category_model import ProductCategoryModel

admin.site.register(ProductCategoryModel)
