from django.test import TestCase
from userYC.models import UserYogaCenter
from .models import CenterAdministratorProfile
from  django.db import IntegrityError
# Create your tests here.
class CenterAdministratorProfileModelTest(TestCase):
    def setUp(self):
        self.user = UserYogaCenter.objects.create(
            username="adminuser",
            first_name="Admin",
            last_name="User",
            email="testadmin@example.com",
            phone="0987654321",
            password="adminpassword")
        self.admin_profile = CenterAdministratorProfile.objects.create(
            user=self.user,
            is_active=True,
            is_firts_created=True,
            is_center_admin=True
        )
    def test_summary_administrator(self):
        summary = self.admin_profile.summary_administrator()
        self.assertEqual(summary["first_name"], "Admin")
        self.assertEqual(summary["last_name"], "User")
        self.assertEqual(summary["email"], "testadmin@example.com")
        self.assertEqual(summary["phone_number"], "0987654321")
        self.assertEqual(summary["is_active"], True)
        self.assertEqual(summary["is_firts_created"], True)
        self.assertEqual(summary["is_center_admin"], True)
    def test_validation_integration(self):
        try:
            CenterAdministratorProfile.objects.create(user_id=9999)
        except IntegrityError:
            print("¡TEST EXCELLENT! The integrity error was caught as expected.")
        except Exception as e:
            print(f"Another error occurred: {e}")       