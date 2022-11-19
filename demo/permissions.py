from rest_framework.permissions import BasePermission

# Данный клас позволяет пользователю управлять только своими материалами


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.user

