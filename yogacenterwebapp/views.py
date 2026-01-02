from django.http import JsonResponse
from django.shortcuts import render

def health_check(request):
    return JsonResponse({'status': 'ok'}, status=200)
def home(request):
    return render(request, '/yogacenterwebapp/home.html')        