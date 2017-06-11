from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_condition import Or
from rest_framework import mixins

import django_filters

from api import models, serializers, permissions


# GET: qualquer um
# POST, PATCH, PUT, DELETE: ninguém
class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


# GET: qualquer um
# POST: qualquer usuário que não tenha cadastro de empresa ainda
# PATCH, PUT: própria empresa, apenas o próprio perfil
# DELETE: apenas deletando o usuário
class EmpresaViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticatedOrReadOnly)
    # Para encontrar dados de determinada empresa basta acrescentar /?search=nome_fantasia
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome_fantasia',)


# Definição do filtro para URL de InteresseEmVaga. Basta acrescentar /?empresa=<cnpj>
class InteresseEmVagaFilter(django_filters.FilterSet):
    empresa = django_filters.CharFilter(name="vaga__empresa")

    class Meta:
        model = models.InteresseEmVaga
        fields = ['empresa']
 

# GET: empresa dona da vaga (através do filtro)
# POST: qualquer um
# PATCH, PUT: ninguém
# DELETE: apenas deletando a vaga
class InteresseEmVagaViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = models.InteresseEmVaga.objects.all()
    permission_classes = (Or(IsAuthenticated, permissions.WriteOnly),)
    serializer_class = serializers.InteresseEmVagaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = InteresseEmVagaFilter


# GET: ninguém
# POST: qualquer um
# PATCH, PUT: próprio usuário no seu perfil
# DELETE: próprio usuário pode deletar sua própria conta
class UsuarioViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = (Or(IsAuthenticated, permissions.WriteOnly),)


# GET: qualquer um
# POST, PATCH, PUT, DELETE: ninguém
class TurnoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Turno.objects.all()
    serializer_class = serializers.TurnoSerializer


# GET: qualquer um
# POST: só empresas
# PATCH, PUT, DELETE: só empresa dona da vaga
# Para encontrar dados de determinada empresa basta acrescentar /id
class VagaViewSet(viewsets.ModelViewSet):
    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer
    permission_classes = (permissions.ManageVacancy,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('empresa', 'curso', 'is_ativa',)
