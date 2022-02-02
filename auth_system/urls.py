from django.urls import path
from .views import loginuser, logoutuser


urlpatterns = [
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('loginuser/', loginuser, name='loginuser'),
]