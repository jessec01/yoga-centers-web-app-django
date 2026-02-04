#instructor/urls.py
from instructor.api import views
from django.urls import path
from instructor.api.views import VerifyEmailView
from instructor.api.views import InstructorRegisterView
from instructor.api.views import InstructorLoginView
# Create your urls here.

pathpatterns = [
    path('api/register/', InstructorRegisterView.as_view(), name='instructor_register'),
    path('api/verify-email/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('api/login/',InstructorLoginView.as_view(), name='instructor_login'),
    ]