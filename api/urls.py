from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views

router = DefaultRouter()
router.register('usuarios', views.UsuarioViewSet)
router.register('empresas', views.EmpresaViewSet)
router.register('vagas', views.VagaViewSet)
router.register('cursos', views.CursoViewSet)
router.register('interesses_vagas', views.InteresseEmVagaViewSet)
router.register('turnos', views.TurnoViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^login/', obtain_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
]
