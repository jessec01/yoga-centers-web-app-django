from django.views.generic.base import TemplateView
from rest_framework.generics import GenericAPIView
#from service.main_service import MainService

# Create your views here.
# Instructor Views
#----------------------------
class InstructorRegisterView(TemplateView):
    # Usar la plantilla genérica de autenticación (registro + login)
    template_name = "instructor/auth_form.html"
class ValidateCodeView(TemplateView):
    template_name = "instructor/validate_code.html"

#login Views
#----------------------------
class InstructorLoginView(TemplateView):
    template_name = "instructor_login.html"
class ValidateLoginView(GenericAPIView):
    pass
 
class dasboaardView(TemplateView):
    template_name = "instructor/dashboard.html"

