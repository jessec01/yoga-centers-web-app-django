from django.db import models
from userYC.models import UserYogaCenter

# Create your models here.
class CenterAdministratorProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_firts_created = models.BooleanField(default=True)
    is_center_admin = models.BooleanField(default=True)
    class Meta:
        db_table = "center_administrator"
    def __str__(self):
        return f"{self.user.username}'s Administrator Profile"