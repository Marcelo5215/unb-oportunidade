from rest_framework import permissions


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False


class ChecarInteressesEmVaga(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.vaga.empresa.usuario_id == request.user.id
        elif request.method == 'POST':
            return True
        return False


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, usuario):
        if request.user:
            return usuario == request.user
        return False


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        elif hasattr(obj, 'id'):
            return obj.id == request.user.id

        else:
            return obj.usuario_id == request.user.id


# class UpdateCompanyProfile(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.usuario_id == request.user.id
