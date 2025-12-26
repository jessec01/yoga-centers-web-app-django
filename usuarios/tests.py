from django.test import TestCase
from usuarios.models import YogaCenterUser, Instructor, Yogui

class UsuarioModelTests(TestCase):
    def test_crear_yoga_center_user(self):
        user = YogaCenterUser.objects.create(
            first_name="Juan",
            last_name="Perez",
            phone_number="123456789",
            password="securepassword",
            email="juan.perez@example.com"
        )
        self.assertEqual(user.first_name, "Juan")
        self.assertEqual(user.last_name, "Perez")
        self.assertEqual(user.phone_number, "123456789")
        self.assertEqual(user.email, "juan.perez@example.com")
        self.assertIsNotNone(user.date_joined)

    def test_crear_instructor(self):
        instructor = Instructor.objects.create(
            first_name="Ana",
            last_name="Gomez",
            phone_number="987654321",
            password="anotherpassword",
            email="ana.gomez@example.com"
        )
        self.assertEqual(instructor.first_name, "Ana")
        self.assertEqual(instructor.last_name, "Gomez")
        self.assertEqual(instructor.phone_number, "987654321")
        self.assertEqual(instructor.email, "ana.gomez@example.com")
        self.assertIsNotNone(instructor.date_joined)

    def test_crear_yogui(self):
        yogui = Yogui.objects.create(
            first_name="Luis",
            last_name="Martinez",
            phone_number="555555555",
            password="yogapassword",
            email="luis.martinez@example.com"
        )
        self.assertEqual(yogui.first_name, "Luis")
        self.assertEqual(yogui.last_name, "Martinez")
        self.assertEqual(yogui.phone_number, "555555555")
        self.assertEqual(yogui.email, "luis.martinez@example.com")
        self.assertIsNotNone(yogui.date_joined)