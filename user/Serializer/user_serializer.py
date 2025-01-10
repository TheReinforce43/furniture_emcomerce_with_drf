from rest_framework import serializers 
from user.models  import User
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import RefreshToken 

# sign up serializer methods
class userSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields = ('id', 'name','phone_number' ,'email', 'password')

    
    def create(self,validated_data):
        password = validated_data['password']
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user 
    

# Login Serializer methods 
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
    phone_number = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)


        # Here check validation 
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        
        if not user.is_active:
            raise serializers.ValidationError('User is not active')
        
        refresh = RefreshToken.for_user(user)

        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone_number': user.phone_number,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            
        }

        # Generate JWT token
         

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

        

    

