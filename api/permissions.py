from rest_framework import permissions

from api.models import InteresseEmVaga, Usuario


class ChecarInteressesEmVaga(permissions.BasePermission):

    def has_permission(self, request, view):
        return InteresseEmVaga.objects.filter(vaga__empresa__usuario=request.user.id)

    # def has_object_permission(self, request, view, obj):
    #     if request.method in permissions.SAFE_METHODS:
    #         return obj.vaga.empresa.usuario_id == request.user.id
    #     elif request.method == 'POST' or request.method == 'DELETE':
    #         return True
    #     return False


class ManageVacancyInterest(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.vaga.empresa.usuario_id == request.user.id
        else:
            return True


class WriteOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return False


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        elif hasattr(obj, 'id'):
            return obj.id == request.user.id

        else:
            return obj.usuario_id == request.user.id


class ManageVacancy(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            # Caso exista usuário de estudante, é preciso fazer 'return request.user.is_empresa'
            return isinstance(request.user, Usuario)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.empresa.usuario == request.user
        return True

# class UpdateCompanyProfile(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.usuario_id == request.user.id
