from django.db import models
from userYC.models import UserYogaCenter
# Create your models here.
class SuperAdminProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=True)
    def summary_super_admin(self):
        return {
            "user_id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,   
            "email": self.user.email,
            "phone_number": self.user.phone,
            "is_active": self.is_active,
            "is_super_admin": self.is_super_admin,
        }
    class Meta:
        db_table = "super_admin"
        
    def __str__(self):
        return f"{self.user.username}'s Super Admin Profile"