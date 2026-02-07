 
from .api.views import (
    AuthFormsView,
    ReadDataView,
    VerifyEmailView,
    ValidateCodeView,
    ControlPanelView,
    HomeView,
    CreateCenterView,
    CustomNotificationsView,
    ReadConfigurationsNotificationView,
    ReportsView,
    GenerateReportView,
    LogoutView, 
)
from django.urls import path

urlpatterns = [
    path('auth/', AuthFormsView.as_view(), name='auth_forms'),
    path('read-data/', ReadDataView.as_view(), name='read_data'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
    path('validate-code/', ValidateCodeView.as_view(), name='validate_code'),
    path('control-panel/', ControlPanelView.as_view(), name='control_panel'),
    path('home/', HomeView.as_view(), name='center_home'),
    path('create-center/', CreateCenterView.as_view(), name='create_center'), 
    path('custom-notifications/', CustomNotificationsView.as_view(), name='custom_notifications'),
    path('read-configurations-notification/', ReadConfigurationsNotificationView.as_view(), name='read_configurations_notification'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('generate-report/', GenerateReportView.as_view(), name='generate_report'),
    path('logout/', LogoutView.as_view(), name='logout'),
]         