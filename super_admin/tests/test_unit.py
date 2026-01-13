
from django.test import TestCase
from userYC.models import UserYogaCenter
from ..models import SuperAdminProfile
from django.db import IntegrityError
from django.core.exceptions import ValidationError    
# Create your tests here.
class SuperAdminProfileModelTest(TestCase):
    def setUp(self):
         
        self.user = UserYogaCenter.objects.create(
        username="superadminuser",
        first_name="SuperAdmin",
        last_name="User",
        email="test@gmail.com",
        phone="+584141234567",
        password="superadminpassword")
  # checkov:skip=CKV_SECRET_6: ADD REASON
        try:    
            self.user.full_clean()
            print("User created and validated successfully.")      
        except ValidationError as e:
            print(f"Validation error while creating user: {e}")    
        
        self.super_admin_profile = SuperAdminProfile.objects.create(
            user=self.user,
            is_active=True,
            is_super_admin=True
        )          
        try:     
            self.super_admin_profile.full_clean()
            print("SuperAdminProfile created and validated successfully.")
        except ValidationError as e:
            print(f"Validation error while creating super admin profile: {e}")    
        
    def test_summary_super_admin(self):
        summary = self.super_admin_profile.summary_super_admin()
        self.assertEqual(summary["first_name"], "SuperAdmin")
        self.assertEqual(summary["last_name"], "User")
        self.assertEqual(summary["email"], "test@gmail.com")
        #self.assertEqual(summary["phone_number"], "1231231234")
        self.assertEqual(summary["is_active"], True)
        self.assertEqual(summary["is_super_admin"], True)
    
