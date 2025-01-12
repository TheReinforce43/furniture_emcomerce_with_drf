from django.db import models 


class AttributeModel(models.Model):

    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(null=True, blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 



