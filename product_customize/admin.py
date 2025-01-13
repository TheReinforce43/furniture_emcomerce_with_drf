from django.contrib import admin

# Register your models here.
from product_customize.Model.attribute_model import AttributeModel 
from product_customize.Model.options_model import OptionModel 
from product_customize.Model.customization_model import ProductCustomizationModel


admin.site.register(AttributeModel)
admin.site.register(OptionModel)
admin.site.register(ProductCustomizationModel)