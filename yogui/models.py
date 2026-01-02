from django.db import models
from userYC.models import UserYogaCenter
class YoguiProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    description_personal = models.TextField(blank=True)
    info_message = models.CharField(max_length=50, blank=True)
    url_profile_picture = models.ImageField()
    is_active = models.BooleanField(default=True)
    point_accumulated = models.IntegerField(default=0)
    is_yogui = models.BooleanField(default=True)
    def sumary_profile(self):
        return {
            "user_id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,   
            "email": self.user.email,
            "phone_number": self.user.phone,
            "description_personal": self.description_personal,
            "info_message": self.info_message,
            "is_active": self.is_active,
            "point_accumulated": self.point_accumulated,
            "is_yogui": self.is_yogui,
        }
    class Meta:
        db_table = "yogui_profile"
    def __str__(self):
        return f"{self.user.username}'s Profile"