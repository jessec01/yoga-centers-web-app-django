from userYC.models import UserYogaCenter
from django.contrib.auth.base_user import BaseUserManager
class Custom_manager(BaseUserManager):
    def create(self,data):
        if not data.get('email'):
            raise ValueError("Email is required")
        if not data.get('username'):
            raise ValueError("Username is required")
        if not data.get('first_name'):
            raise ValueError("First name is required")
        if not data.get('last_name'):
            raise ValueError("Last name is required")
        if not data.get('password'):
            raise ValueError("Password is required")
        if not data.get('phone'):
            raise ValueError("Phone number is required")
        email=self.normalize_email(data['email'])
        user=self.model(email=email,username=data['username'],first_name=data['first_name'],last_name=data['last_name'],phone=data['phone'])
        if data.get('password'):
            user.set_password(data['password'])
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user
    def create_superuser(self,data):
        data['is_staff']=True
        data['is_superuser']=True
        data['is_active']=True
        if data.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        return self.create(data)