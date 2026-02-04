from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from super_admin.api.views import ReadFormView
class SuperAdminIntegrationTest(APITestCase):
    
    def setUp(self):
        self.client = APIClient() #
    def test_create_super_admin(self):
        self.factory = APIRequestFactory('api/readregister/')
        self.view = ReadFormView.as_view()
        self.response = self.client.post('/super_admin/api/readregister/', {
            "username": "mismatch_test",
  "first_name": "Jessec",
  "last_name": "Zuleta",
  "email": "mismatch@example.com",
  "phone": "+582617001122",
  "password": "Valida123!",
  "confirmation_password": "OtraValida_1!"
            
        }, format='json')
        #assert ReadFormView.objects.count() == 1
        if self.response.status_code != 201:
            print("Response data:", self.response.data)
        else:
            print("Super admin created successfully:", self.response.data)
        """self.assertEqual(self.response.status_code, 201) 
        self.assertIn('id', self.response.data)
        self.assertEqual(self.response.data['user']['username'], 'testuser')
        self.assertEqual(self.response.data['user']['email'], 'testuser@example.com')"""    