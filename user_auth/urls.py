from django.urls import path
from .views import *

urlpatterns = [
    path('user/register',user_register,name='user.register'),
    path('user/login',user_login,name='user.login'),
    path('user/logout',user_logout,name='user.logout'),
]