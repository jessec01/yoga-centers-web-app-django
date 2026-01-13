#super_admin/views.py

from django.views.generic.base import TemplateView
from rest_framework.permissions import AllowAny as allow_any
from userYC.models import UserYogaCenter
from rest_framework.generics import CreateAPIView
from super_admin.api.createserializer import SuperAdminCreateSerializer
#define la vista del formulario de registro
class FormRegisterView(TemplateView):
    template_name = "super_admin/register_view.html"
#definir la vista para procesar la respuesta del formulario     
#define la vista del perfil del super admin
class ReadFormView(CreateAPIView):

    queryset = UserYogaCenter.objects.all()
    serializer_class = SuperAdminCreateSerializer
    permission_classes = [allow_any]  # Permitir acceso sin autenticación
class SuperAdminSessionView(TemplateView):
    template_name = "super_admin_session.html"