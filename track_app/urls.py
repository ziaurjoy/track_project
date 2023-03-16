from django.urls import path
from . import views

urlpatterns = [
    path('user-registration-api/', views.UserRegistrationAPI.as_view(), name='user-registration-api'),
    path('device-api/', views.DeviceCreateListAPI.as_view(), name='device-api'),
    path('device-details-api/<int:pk>/', views.DeviceDetail.as_view(), name='device-details-api'),

]
