from django.db import models 

# import related models 
from user.models import User 


class CartModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_cart')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)