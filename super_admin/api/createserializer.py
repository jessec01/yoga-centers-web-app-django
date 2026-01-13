#super_admin/api/createserializer.py
import re
from super_admin.service.group_data import GroupDataService
from super_admin.service.create_transaction import CreateTransactionService as CreateTransaction
from userYC.models import UserYogaCenter    
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer  
from phonenumber_field.phonenumber import to_python

#Definir el serializador para crear un super admin
class SuperAdminCreateSerializer(ModelSerializer):
    #definir los campos del serializador
    confirmation_password=serializers.CharField(write_only=True)
    class Meta:
        #definir los modelos a utilizar
        model=UserYogaCenter
        field=['username','first_name','last_name','email','phone','password']
        fields='__all__'
        #definir restricciones para los campos
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self,value_username):
        usernameRegex = re.search('^(?=.*[a-zA-Z])(?!.*[#$<>])[a-zA-Z0-9_]{4,16}$',value_username)
        if not usernameRegex:
            raise serializers.ValidationError({"username": "invalid username"})
            pass
        return value_username 
    def validate_first_name(self,value_first_name):
        first_name=re.search('^[a-zA-Z]{4,16}$',value_first_name)
        if not first_name:
            raise serializers.ValidationError({"first name": "invalid name"})
        return value_first_name 
    def validate_last_name(self,value_last_name):
        last_name=re.search('^[a-zA-Z]{4,16}$',value_last_name)
        if not last_name:
            raise serializers.ValidationError({"last_name": "invalid last name"})
        return value_last_name 
    def validate_phone(self, value):
        value = to_python(value)
        if not value.is_valid():
            raise serializers.ValidationError({"phone":"Invalid phone number."}) 
        return value
    def validate_email(self,value_email):
        email=re.search('^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$',value_email)
        if not email:
            raise serializers.ValidationError({"email": "invalid email"})
        return value_email 
    def validate_password(self,value_password):
        password=re.search("^(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).{8,16}+$",value_password)
        if not password:
             raise serializers.ValidationError({"password": "strong password required"})
        return value_password 
    def validate(self,attrs):
        password=attrs.get('password') 
        confirmation_password=attrs.get('confirmation_password')
        if password!=confirmation_password:
            
            raise serializers.ValidationError({"confirmation_password": "passwords do not match"})  
        return attrs 
    def create(self, validated_data):
        #crear el usuario
        username=validated_data['username']
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        email=validated_data['email']
        phone=validated_data['phone']
        password=validated_data['password']
        data = GroupDataService.group_data(username, first_name, last_name, email, phone, password)
        super_admin_profile=CreateTransaction.receiver_data(self,data)
        #crear el perfil de super admin
        
        return super_admin_profile
    
    #se definira validaciones mas estrictas despues del primer 
    #testing de integracion 