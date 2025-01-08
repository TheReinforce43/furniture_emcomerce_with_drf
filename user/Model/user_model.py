from django.db import models 
from django.contrib.auth.models import AbstractUser 


from user.custom_manager import UserManager



class User(AbstractUser):

    username = None  # Disable username as we are using email as the identifier
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, max_length=100)
    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)  # To differentiate between customers and staff
    is_customer = models.BooleanField(default=True)  # To identify if a user is a customer
    is_active = models.BooleanField(default=True)  # For account activation status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['name', 'phone_number']  # Fields required for creating a new user account

    objects = UserManager()

    def __str__(self):
        return self.email


