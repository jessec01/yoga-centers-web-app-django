from django.db import models
from userYC.models import UserYogaCenter

# Create your models here.
class CenterAdministratorProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_firts_created = models.BooleanField(default=True)
    is_center_admin = models.BooleanField(default=True)
    def summary_administrator(self):
        return {
            "user_id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,   
            "email": self.user.email,
            "phone_number": self.user.phone,
            "is_active": self.is_active,
            "is_firts_created": self.is_firts_created,
            "is_center_admin": self.is_center_admin,
        }
    class Meta:
        db_table = "center_administrator"
    def __str__(self):
        return f"{self.user.username}'s Administrator Profile"