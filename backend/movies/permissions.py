from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        # Autoriser uniquement si l'utilisateur est un administrateur
        return request.user.is_authenticated and request.user.userrole.role == 'admin'
