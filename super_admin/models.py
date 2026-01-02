from django.db import models
from userYC.models import UserYogaCenter
# Create your models here.
class SuperAdminProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_super_admin = models.BooleanField(default=True)
    class Meta:
        db_table = "super_admin"
        
    def __str__(self):
        return f"{self.user.username}'s Super Admin Profile"