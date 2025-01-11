from django.db import models 


class ProductCategoryModel(models.Model):

    category_name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f' category_name : {self.category_name}'