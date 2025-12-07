# api/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Чтение разрешено всем (безопасные методы: GET, HEAD, OPTIONS)
        # Изменение — только авторизованным
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        # Чтение — всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение — только автору объекта
        return obj.author == request.user