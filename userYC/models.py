#userYC/models.py
#  se immporta el modelo propio de ActrabtUser y se extiende para agregar el campo phone
#se instala y define el paquete phonenumber_field para manejar numeros telefonicos 
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserYogaCenter(AbstractUser):
    phone = PhoneNumberField(blank=True, help_text='Contact phone number')

    class Meta:
        verbose_name = "UserYC"
        verbose_name_plural = "UsersYC"