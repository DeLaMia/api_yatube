from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
