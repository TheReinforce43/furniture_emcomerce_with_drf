from rest_framework import serializers 
from user.Model.user_model import User 
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken 

# sign up serializer methods
class userSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ('id', 'username','phone_number' ,'email', 'password')

    
    def create(self,validated_data):
        password = validated_data['password']
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user 
    

# Login Serializer methods 

class UserLoginSerializer(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def  validate(self,data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        
        # Generate JWT token

        refresh = RefreshToken.for_user(user)

        return {
            'id':user.id,
            'username': user.username,
            'email': user.email,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }
    

# Log Out Serializer  


class LogOutSerializer(serializers.Serializer):

    RefreshToken = serializers.CharField()

    def validate(self,data):
        self.RefreshToken= data.get('RefreshToken')
        return data 
    
    def save(self,**kwargs):

        try:
            token = RefreshToken(self.RefreshToken)
            token.blacklist()
        
        except Exception as e:
            raise serializers.ValidationError('Invalid token or expire')

        

    

