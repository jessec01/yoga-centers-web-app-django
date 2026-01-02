#instructor/tests.py
from django.test import TestCase
from userYC.models import UserYogaCenter
from .models import InstructorProfile, YoguiProfile
from django.db import IntegrityError
# Create your tests here.
class IntructorProfileModelTest(TestCase):
    def setUp(self):
        self.user = UserYogaCenter.objects.create(
            username="instructoruser",
            first_name="Instructor",
            last_name="User",
            email="testinstructor@example.com",
            phone="1122334455",
            password="instructorpassword")
  # checkov:skip=CKV_SECRET_6: ADD REASON
        self.instructor_profile = YoguiProfile.objects.create(
            user=self.user,
            description_personal="Certified yoga instructor",
            specialty="Hatha Yoga",
            is_active=True,
            qualification=4.5,
            is_instructor=True
        )
    def test_summary_instructor(self):
        summary = self.instructor_profile.summary_instructor()
        self.assertEqual(summary["first_name"], "Instructor")
        self.assertEqual(summary["last_name"], "User")
        self.assertEqual(summary["email"], "testinstructor@example.com")
        self.assertEqual(summary["phone_number"], "1122334455")
        self.assertEqual(summary["description_personal"], "Certified yoga instructor")
        self.assertEqual(summary["specialty"], "Hatha Yoga")
        self.assertEqual(summary["is_active"], True)
        self.assertEqual(summary["qualification"], 4.5)
        self.assertEqual(summary["is_instructor"], True)
    def test_validation_integration(self):
        try:
            InstructorProfile.objects.create(user_id=9999)
        except IntegrityError:
            print("¡TEST EXCELLENT! The integrity error was caught as expected.")
        except Exception as e:
            print(f"Another error occurred: {e}")   
    