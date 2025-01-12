from django.db import models 

from product_customize.Model.attribute_model import AttributeModel


class OptionModel(models.Model):

    option_name = models.CharField(max_length=200)
    attribute=models.ForeignKey(AttributeModel,related_name="option_text",on_delete=models.CASCADE,db_index=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.option_name}'
    
