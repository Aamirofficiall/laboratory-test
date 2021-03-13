from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auths import models

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
class ChangePasswordSerializer(serializers.Serializer):
	old_password = serializers.CharField(max_length=128, write_only=True, required=True)
	new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
	new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

	def validate_old_password(self, value):
		user = self.context['request'].user
		if not user.check_password(value):
			raise serializers.ValidationError(
				_('Your old password was entered incorrectly. Please enter it again.')
			)
		return value

	def validate(self, data):
		if data['new_password1'] != data['new_password2']:
			raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
		password_validation.validate_password(data['new_password1'], self.context['request'].user)
		return data

	def save(self, **kwargs):
		password = self.validated_data['new_password1']
		user = self.context['request'].user
		user.set_password(password)
		user.save()
		try:
			user.auth_token.delete()
			token, created = Token.objects.get_or_create(user=user)
			return Response({'token': token.key})
		except:
			pass
		return user


class UserProfileSerializer(serializers.ModelSerializer):
	"""Serializes a user profile object"""

	class Meta:
		model = User
		fields = ('id', 'email','password','confirm_password',)
		#make password write only true cannot retrive it
		extra_kwargs = {
			'password': {
				'write_only': True,
				'style': {'input_type': 'password'}
			},

			'confirm_password': {
				'write_only': True,
				'style': {'input_type': 'password'}
				
			}
		}
		
	def validate(self, validated_data):
		if validated_data.get('password') != validated_data.get('confirm_password'):
			raise serializers.ValidationError("Those passwords don't match.")
		return validated_data
	 
	


