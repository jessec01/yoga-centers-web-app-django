from django.db import models
from userYC.models import UserYogaCenter
class YoguiProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    description_personal = models.TextField(blank=True)
    experience_level = models.CharField(max_length=50, blank=True)
    url_profile_picture = models.ImageField()
    is_active = models.BooleanField(default=True)
    point_accumulated = models.IntegerField(default=0)
    is_yogui = models.BooleanField(default=True)
    class Meta:
        db_table = "yogui_profile"
    def __str__(self):
        return f"{self.user.username}'s Profile"