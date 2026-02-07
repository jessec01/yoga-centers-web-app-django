#userYC/models.py
#Se importa el modelo propio de AbstractUse y se extiende para agregar el campo phone
#se instala y define el paquete phonenumber_field para manejar numeros telefonicos 
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
class UserYogaCenter(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=False,null=False,unique=True, max_length=255)
    username = models.CharField(blank=False,null=False,max_length=150, unique=True)
    first_name = models.CharField(null=False,blank=False,max_length=30)
    last_name = models.CharField(blank=False,null=False,max_length=30) 
    password = models.CharField(blank=False,null=False,max_length=128)
    phone = PhoneNumberField(blank=False,null=False,unique=True,help_text='Contact phone number',region='VE')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_yogui = models.BooleanField(default=False)
    is_admin_center = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user_yoga_center"
    
    def __str__(self):
        return self.username