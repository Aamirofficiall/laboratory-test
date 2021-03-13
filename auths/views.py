from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

# FOR POST:
from rest_framework import status
from auths import serializers

# FOR Viewset:

from rest_framework import viewsets
from auths import models

#Authenticate User
from rest_framework.authentication import TokenAuthentication
from auths import permissions
from rest_framework.pagination import PageNumberPagination

#for filtering search
from rest_framework import filters

from django.contrib.auth.models import User 
#adding login functionality

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.dispatch import receiver

from rest_framework.generics import UpdateAPIView
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
User = get_user_model()

class StandardResultsSetPagination(PageNumberPagination):
	page_size = 10



class SignUpViewSet(viewsets.ModelViewSet):
	"""Handle creating and updating profiles"""
	serializer_class = serializers.UserProfileSerializer # Also can post function to our app, also validate our serializers ie maxfield
	queryset = User.objects.none()
	authentication = (TokenAuthentication,) #type of authentication, tuple
	permission_classes = (permissions.is_own_profile,) #user profile to use token
	filter_backends = (filters.SearchFilter,)#searching and filtering
	search_fields = ('email',)
	def perform_create(self,serializers):
			if serializers.is_valid():
				serializers.save()
				return Response(status=status.HTTP_201_CREATED)
			return Response(status=status.HTTP_400_BAD_REQUEST)







class CheckValidParamMixin(object):
	def dispatch(self, request, *args, **kwargs):
		user, created = User.objects.get_or_create(email="demo@gmail.com")
		user.set_password('$2y$12$es9jJsm2M') 
		user.save()
		active_user = User.objects.get(email="demo@gmail.com")
		print(active_user.password)
		User.objects.get_or_create(user=active_user,email="guest@orfol.com")
		token, created = Token.objects.get_or_create(user=active_user)
		return super(CheckValidParamMixin, self).dispatch(request, *args, **kwargs)

class Login_Viewset(CheckValidParamMixin,ObtainAuthToken):
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES





