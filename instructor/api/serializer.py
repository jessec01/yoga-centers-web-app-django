#super_admin/api/createserializer.py
import re
from userYC.service.group_data import GroupDataService
from userYC.models import UserYogaCenter    
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer  
from phonenumber_field.phonenumber import to_python
from instructor.models import InstructorProfile
from magiclink.service.tokenmagiclink import TokenLinkService
from service.register.datapreparer import DataPreparerService
#Definir el serializador para crear un super admin
class InstructorCreateSerializer(ModelSerializer):
    