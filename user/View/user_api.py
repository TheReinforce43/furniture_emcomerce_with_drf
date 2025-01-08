from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated


from user.Serializer.user_serializer import (
    userSignUpSerializer,
    LogOutSerializer,
    UserLoginSerializer
)




# User Sign Up Registration 

class SignUpView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = userSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# login api  view 

class LoginView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# log out api user


class LogoutAPI(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer = LogOutSerializer(data= request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"You log out successfully"},status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

