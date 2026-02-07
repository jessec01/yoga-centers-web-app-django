#magiclink/models.py
from django.db import models
from userYC.models import UserYogaCenter    
# Create your models here.
class MagicLink(models.Model):
    id_user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    jti_token = models.CharField(max_length=255, unique=True) 
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    key_code=models.CharField(max_length=6, unique=True)
    is_used = models.BooleanField(default=False)
    def __str__(self):
        return f"MagicLink for {self.email} - Used: {self.is_used}"
    def mark(self):
        self.is_used = True
        self.save()
    def mark_as_used(self):
        return True if self.is_used else False
    