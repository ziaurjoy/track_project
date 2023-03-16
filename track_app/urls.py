from django.urls import path
from . import views

urlpatterns = [
    path('user-registration-api/', views.UserRegistrationAPI.as_view(), name='user-registration-api'),
    path('device-api/', views.DeviceCreateListAPI.as_view(), name='device-api'),
    path('device-details-api/<int:pk>/', views.DeviceDetailAPI.as_view(), name='device-details-api'),

    path('employee-api/', views.EmployeeCreateListAPI.as_view(), name='employee-api'),
    path('employee-details-api/<int:pk>/', views.EmployeeDetailAPI.as_view(), name='employee-details-api'),

    path('track-api/', views.TrackCreateListAPI.as_view(), name='employee-api'),
    path('track-details-api/<int:pk>/', views.TrackDetailAPI.as_view(), name='employee-details-api'),

]
