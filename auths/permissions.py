from rest_framework import permissions


class is_own_profile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #only if get request
            return True

        return obj.id == request.user.id #check if user post on its own id

class UserPermissionsAll(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.user.is_staff:
			return True
		else:
			return False

	#Owners of the object or admins can do anything Everyone else can do nothing
class IsAuthenticated(permissions.IsAuthenticated):

	def has_object_permission(self, request, view, obj):
		return self.has_permission(request, view) and obj.id == request.user.id	
	#Owners of the object or admins can do anything Everyone else can do nothing
class IsNotGuest(permissions.IsAuthenticated):
	def has_object_permission(self, request, view, obj):
		return self.has_permission(request, view) and obj.phone_number !="98761234567" and request.user.phone_number!="98761234567"