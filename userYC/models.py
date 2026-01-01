#userYC/models.py
from django.db.models        import ActrabtUser
from phonenumber_field           import PhoneField
# Create your models here.
class UserYogaCenter(ActrabtUser):
    phone=PhoneField(blank=True, help_text='Contact phone number')
    class Meta:
        proxy = True
        verbose_name = "UserYC"
        verbose_name_plural = "UsersYC"