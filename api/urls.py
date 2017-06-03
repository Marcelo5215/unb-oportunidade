from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# Remover! Usuários não terão acesso aos outros usuários, apenas a Estudante ou Empresa.
router.register('usuarios', views.UsuarioViewSet)   # ModelViewSet não precisa de base_name.

urlpatterns = [
    url(r'', include(router.urls))
]
