from django.urls import path, include
from auths import views
#ROUTER FOR VIEWSET, different from api 
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User

router = DefaultRouter()

router.register('signup', views.SignUpViewSet, 'signup')


urlpatterns = [
	path('',include(router.urls)),
	path('login/',views.Login_Viewset.as_view(),name='login'),

   ]
