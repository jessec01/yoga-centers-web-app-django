from super_admin.api import views
from django.urls import path
urlpatterns = [
    path('api/formregister/', views.FormRegisterView.as_view(), name='super_admin_register'),
    path('api/readregister/', views.ReadFormView.as_view(), name='super_admin_api_register'),
    path('session/', views.SuperAdminSessionView.as_view(), name='super_admin_session'),
]