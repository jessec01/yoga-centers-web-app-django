from django.db import transaction
from usuarios.models import YogaCenterUser, Instructor, Yogui
from django.contrib.auth.hashers import make_password

def crear_instructor(data):
    with transaction.atomic():
        user = YogaCenterUser.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            password=make_password(data['password']),
            email=data['email']
        )
        instructor = Instructor.objects.create(
            id=user.id,
            specialty=data['specialty'],
            years_of_experience=data['years_of_experience'],
            score=data['score'],
            profile_picture=data.get('profile_picture')
        )
    return instructor

def crear_yogui(data):
    with transaction.atomic():
        user = YogaCenterUser.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number'],
            password=make_password(data['password']),
            email=data['email']
        )
        yogui = Yogui.objects.create(
            id=user.id,
            id_number=data['id_number'],
            membership_level=data['membership_level'],
            profile_picture=data.get('profile_picture')
        )
    return yogui