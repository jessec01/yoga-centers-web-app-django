from django.db import models

class YogaCenterUser(models.Model):
    first_name = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Instructor(YogaCenterUser):
    specialty = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    score = models.FloatField()
    profile_picture = models.ImageField(upload_to='instructors/', null=True)

    class Meta:
        db_table = 'instructors'
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Instructor"


class Yogui(YogaCenterUser):
    id_number = models.CharField(max_length=50, unique=True)
    membership_level = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='yoguis/', null=True, blank=True)

    class Meta:
        db_table = 'yoguis'
        verbose_name = 'Yogui'
        verbose_name_plural = 'Yoguis'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Yogui"