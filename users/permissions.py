from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Класс для проверки является ли Пользователь Владельцем.
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
    Предполагается, что экземпляр модели имеет атрибут «владелец».
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if obj.owner == request.user:
            return True
        return False
