from django.test import TestCase

import yogui
from .models import YoguiProfile
from django.db import IntegrityError
# Create your tests here.
class YoguiProfileModelTest(TestCase):
    def setUp(self):
        self.user = yogui.models.UserYogaCenter.objects.create(
            username="testuser",
            first_name="Test",
            last_name="User",
            email="testuser@example.com",
            phone="1234567890",
            password="testpassword")   

        self.yogui_profile = YoguiProfile.objects.create(
            user=self.user,
            description_personal="Experienced yoga instructor",
            info_message="Welcome to my profile!",
            url_profile_picture="path/to/picture.jpg",
            is_active=True,
            point_accumulated=100,
            is_yogui=True
        )
    def test_sumary_profile(self):
        summary = self.yogui_profile.sumary_profile()
        self.assertEqual(summary["description_personal"], "Experienced yoga instructor")
        self.assertEqual(summary["info_message"], "Welcome to my profile!")
        self.assertEqual(summary["is_active"], True)
        self.assertEqual(summary["point_accumulated"], 100)
        self.assertEqual(summary["is_yogui"], True)
    def test_validation_integration(self):
        try:
            YoguiProfile.objects.create(user_id=9999, url_profile_picture="fantasma.jpg")
        except IntegrityError:
            print("¡TEST EXCELLENT! The integrity error was caught as expected.")
        except Exception as e:
            print(f"Another error occurred: {e}")