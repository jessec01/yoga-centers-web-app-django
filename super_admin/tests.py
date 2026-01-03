from django.test import TestCase
from userYC.models import UserYogaCenter
from .models import SuperAdminProfile
from django.db import IntegrityError    
# Create your tests here.
class SuperAdminProfileModelTest(TestCase):
    def setUp(self):
        self.user = UserYogaCenter.objects.create(
            username="superadminuser",
            first_name="SuperAdmin",
            last_name="User",
            email="test@gmail.com",
            phone="1231231234",
            password="superadminpassword")
        self.super_admin_profile = SuperAdminProfile.objects.create(
            user=self.user,
            is_active=True,
            is_super_admin=True
        )               
    def test_summary_super_admin(self):
        summary = self.super_admin_profile.summary_super_admin()
        self.assertEqual(summary["first_name"], "SuperAdmin")
        self.assertEqual(summary["last_name"], "User")
        self.assertEqual(summary["email"], "test@gmail.com")
        self.assertEqual(summary["phone_number"], "1231231234")
        self.assertEqual(summary["is_active"], True)
        self.assertEqual(summary["is_super_admin"], True)
    def test_validation_integration(self):
        try:
            SuperAdminProfile.objects.create(user_id=9999)
        except IntegrityError:
            print("¡TEST EXCELLENT! The integrity error was caught as expected.")
        except Exception as e:
            print(f"Another error occurred: {e}")  
