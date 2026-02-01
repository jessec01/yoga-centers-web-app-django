from django.views.generic.base import TemplateView

from service.main_service import MainService

# Create your views here.
class InstructorRegisterView(TemplateView):
    template_name = "instructor/register_view.html" 
class InstructorLoginView(TemplateView):
    template_name = "instructor_session.html"

class SessionInstructorView(TemplateView):
    mainservice=MainService()
    try:
        queryset =mainservice.get_all_instructors()
        serializer_class = mainservice.get_serializer()
        mainservice.validation_credentials(serializer_class)  
        mainservice.run_authentication()
    except Exception as e:
        print (f"Error initializing SessionInstructorView: {e}")