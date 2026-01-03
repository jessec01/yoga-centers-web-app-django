from django.db import models
from userYC.models import UserYogaCenter
# Create your models here.
class InstructorProfile(models.Model):
    user = models.OneToOneField(UserYogaCenter, on_delete=models.CASCADE)
    description_personal = models.TextField(blank=True)
    specialty = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='instructor_pics/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    qualification = models.FloatField(default=0.0)
    is_instructor = models.BooleanField(default=True)
    def summary_instructor(self):
        return {
            "user_id": self.user.id,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,   
            "email": self.user.email,
            "phone_number": self.user.phone,
            "description_personal": self.description_personal,
            "specialty": self.specialty,
            "is_active": self.is_active,
            "qualification": self.qualification,
            "is_instructor": self.is_instructor,
        }
    class Meta:
        db_table = "instructor_profile"
    def __str__(self):
        return f"{self.user.username}'s Instructor Profile"
