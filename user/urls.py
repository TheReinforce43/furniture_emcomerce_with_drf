from django.urls import path 

from user.View.user_api import (
    SignUpView,
    LoginView,
    LogoutAPI,
)

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),  # Logout API endpoint
]
