from django.views.generic.base import TemplateView
from rest_framework.views import APIView
#registro y login de administradores del centro
class AuthFormsView(TemplateView):
    template_name = "center_administrator/auth_form.html"
#vista para la creacion de datos iniciales del centro
#ademas genera el token de codigo para verificar el correo electronico
class ReadDataView(APIView):
    pass
#vista para verificar el correo electronico
class VerifyEmailView(TemplateView):
    template_name = "center_administrator/verify_email.html"
#valida lo codigo enviado al correo electronico
class ValidateCodeView(APIView):
    pass

#valida el tipo de session del administrador del centro
class ControlPanelView(TemplateView):
    template_name = "center_administrator/control_panel.html"
#vista principal del administrador del centro
class HomeView(TemplateView):
    template_name = "center_administrator/              Centerhome.html"

class CreateCenterView(TemplateView):
    template_name = "center_administrator/create_center.html"
class CustomNotificationsView(TemplateView):
    template_name = "center_administrator/custom_notifications.html"
#leer las configuraciones de notificaciones
class ReadConfigurationsNotificationView(APIView):
    pass
#muestra los reportes del centro
class ReportsView(TemplateView):
    template_name = "center_administrator/reports.html"
#vista para generar reportes pdf
class GenerateReportView(APIView):
    pass

#vista para cerrar session
class LogoutView(APIView):
    pass