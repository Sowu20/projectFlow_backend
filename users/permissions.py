from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    
class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'client'
    
class IsColaborateur(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'collaborateur'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'