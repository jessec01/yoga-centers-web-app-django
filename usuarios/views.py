from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .services import crear_instructor, crear_yogui
from .models import Instructor, Yogui

def registrar_instructor(request):
    if request.method == 'POST':
        data = request.FILES.dict()
        try:
            instructor = crear_instructor(data)
            return redirect('instructor_exito')
        except Exception as e:
            return render(request, 'usuarios/registro_instructor.html', {
                'error': str(e),
                'data': data
            })
    return render(request, 'usuarios/registro_instructor.html')

def registrar_yogui(request):
    if request.method == 'POST':
        data = request.FILES.dict()
        try:
            yogui = crear_yogui(data)
            return redirect('yogui_exito')
        except Exception as e:
            return render(request, 'usuarios/registro_yogui.html', {
                'error': str(e),
                'data': data
            })
    return render(request, 'usuarios/registro_yogui.html')

class InstructorExitoView(TemplateView):
    template_name = 'usuarios/instructor_exito.html'

class YoguiExitoView(TemplateView):
    template_name = 'usuarios/yogui_exito.html'

def lista_intructores(request):
    instructores = Instructor.objects.all()
    return render(request, 'usuarios/lista_instructores.html', {'instructores': instructores})
    
def lista_yoguis(request):
    yoguis = Yogui.objects.all()
    return render(request, 'usuarios/lista_yoguis.html', {'yoguis': yoguis})