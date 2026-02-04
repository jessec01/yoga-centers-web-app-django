from re import re
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from instructor.models import Instructor
class LoginSerializer(ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['usernanme', 'password']
        def validate_username(self,value_username):
            usernameRegex = re.search('^(?=.*[a-zA-Z])(?!.*[#$<>])[a-zA-Z0-9_]{4,16}$',value_username)
            if not usernameRegex:
                raise serializers.ValidationError({"username": "invalid username"})
            
            return value_username
    
        def validate_password(self,value: str)-> str:
            if not value:
                raise serializers.ValidationError("Password is required")
            return value
        

            