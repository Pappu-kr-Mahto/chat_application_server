from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['first_name' , 'last_name' , 'email', 'password' ]

        def validate(self,data):
            if CustomUserModel.objects.filter(email = data['email']).exists():
                raise serializers.ValidationError('User already exists with this username/email')
            return data
