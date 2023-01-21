from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user :
            return True 

class IsAdminPermission(permissions.BasePermission):
    edit_methods = ('CREATE')
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True 
        return False           
