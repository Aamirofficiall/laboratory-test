from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *
from .views_web import *

from django.urls import path,include
from django.conf.urls import url, include

from django.contrib.auth.views import (LoginView,LogoutView ,
                                       PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView)
from .views_web import register,home,UpdateUser,UpdatePassword
urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='auth_register'),
]

urlpatterns = [
    path('',home,name='home'),
    path('register/',register, name='register'),
    path('update/',UpdateUser,name="update"),
    path('password/',UpdatePassword,name="password"),
    path('login/',LoginView.as_view(template_name= 'login.html'), name='login-web'),
    path('logout/',LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    url(r'^reset-password/$', PasswordResetView.as_view(template_name= 'reset_password.html'), name='reset_password'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(template_name= 'reset_password_done.html'), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name= 'reset_password_confirm.html'), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name='password_reset_complete'),

# api urls 
    path('api/register/', RegisterView.as_view(), name='auth_register'),

    
]