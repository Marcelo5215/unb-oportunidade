# from django.core.validators import validate_email
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# class SearchVacancy(APIView):
#     def get(self, request, format=None):
#         vacancy = VacantJob.objects.all()
#
#         # Parametro icreated: data de insercao minima (deve ser passada no formato YYYYMM)
#         if 'icreated' in request.GET:
#             try:
#                 # Transforma parametro em objeto datetime para ser usado no filtro
#                 creationDate = datetime.datetime.strptime(request.GET.get('icreated'), '%Y%m')
#             except ValueError:
#                 return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")
#
#             vacancy = vacancy.filter(created_at__date__gte=creationDate)
#
#         # Parametro fcreated: data de insercao maxima (deve ser passada no formato YYYYMM)
#         if 'fcreated' in request.GET:
#             try:
#                 # Transforma parametro em objeto datetime para ser usado no filtro
#                 creationDate = datetime.datetime.strptime(request.GET.get('fcreated'), '%Y%m')
#             except ValueError:
#                 return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")
#
#             vacancy = vacancy.filter(created_at__date__lte=creationDate)
#
#         # Parametro course: Curso da vaga (deve ser passada abreviacao do curso)
#         if 'course' in request.GET:
#             courses = [VacantJobHasCourse.vacant_job_id_id for VacantJobHasCourse in
#                        VacantJobHasCourse.objects.all().filter(course_id__abbreviation=request.GET.get('course'))]
#             vacancy = vacancy.filter(id_vacancy__in=courses)
#
#         # Parametro company: Nome da empresa que oferece a vaga
#         if 'company' in request.GET:
#             companies = [Hiring.id_vacancy_id for Hiring in
#                          Hiring.objects.filter(id_company__name__icontains=request.GET.get('company'))]
#             vacancy = vacancy.filter(id_vacancy__in=companies)
#
#         vacancy = [VacantJob.role for VacantJob in vacancy]
#
#         return Response(vacancy)


# User = get_user_model()

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permissions_classes = [AllowAny]


# from .serializers import UserSerializer, StudentSerializer, CompanySerializer
# import datetime

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import mixins

from api import models, serializers, permissions
# from rest_framework.DjangoFilterBackend import DjangoFilterBackend
# from django.http import HttpResponse, Http404, JsonResponse
#
# from rest_framework.renderers import JSONRenderer
# from rest_framework import generics
# from rest_framework.response import Response

# foi necessario importar cada nome da tabela usada nas querys de busca
# porque caso eu nao fizesse isso, teria que acessar as tabelas por: models.Empresa . 
# Só que dessa forma dá o seguinte erro: Manager isn't accessible via topic instance
# Quando tento fazer a mesma query duas vezes seguidas.
# from api.models import (
#      Empresa,
#      Curso,
#      Vaga,
# )

# from api.serializers import (
#      CursoSerializer,
#      EmpresaSerializer,
#      VagaSerializer,
# )


# Create your views here.

# Lista Todos os cursos presentes na base de dados
# class ListCourses(generics.ListAPIView):
#     queryset = Curso.objects.all()
#     serializer_class = CursoSerializer
#     filter_backends = (DjangoFilterBackend,)
#     search_fields = ('nome')
#
# # Lista Todas as empresas presentes na base de dados
# class ListCompanies(generics.ListAPIView):
#     queryset = Empresa.objects.all()
#     serializer_class = EmpresaSerializer
#     filter_backends = (DjangoFilterBackend,)
#     search_fields = ('nome')
#
# # Lista Todas as empresas presentes na base de dados
# class ListVacantJob(generics.ListAPIView):
#     queryset = Vaga.objects.all()
#     serializer_class = VagaSerializer
#     filter_backends = (DjangoFilterBackend,)
#     search_fields = ('titulo')
#
# #Busca se uma determinada empresa existe na base de dados
# class SearchCompany(generics.ListAPIView):
#     def get(self, request, nome=None):
#         #Parametro name: Nome da Empresa
#         try:
#             empresa = [Empresa.nome for Empresa in Empresa.objects.filter(nome=nome)]
#         except Empresa.DoesNotExist:
#             empresa = None
#
#         return Response(empresa)

# GET: qualquer um
# POST, PATCH, PUT: ninguém
class CursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Curso.objects.all()
    serializer_class = serializers.CursoSerializer


# GET: qualquer um
# POST: qualquer um
# PATCH, PUT: própria empresa, apenas o próprio perfil
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = models.Empresa.objects.all()
    serializer_class = serializers.EmpresaSerializer
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticatedOrReadOnly)
    # Para encontrar dados de determinada empresa basta acrescentar /?search=nome_fantasia
    filter_backends = (filters.SearchFilter,)
    search_fields = ('nome_fantasia',)


# GET: empresa dona da vaga
# POST: qualquer um
# PATCH, PUT: ninguém
class InteresseEmVagaViewSet(viewsets.ModelViewSet):
    queryset = models.InteresseEmVaga.objects.all()
    permission_classes = (permissions.ChecarInteressesEmVaga,)
    serializer_class = serializers.InteresseEmVagaSerializer


# GET: ninguém
# POST: qualquer um
# PATCH, PUT: próprio usuário no seu perfil
# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = models.Usuario.objects.all()
#     serializer_class = serializers.UsuarioSerializer
#     permission_classes = (permissions.UpdateOwnProfile,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('email',)
class UsuarioViewSet(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email',)


# GET: qualquer um
# POST, PATCH, PUT: ninguém
class TurnoViewSet(viewsets.ModelViewSet):
    queryset = models.Turno.objects.all()
    serializer_class = serializers.TurnoSerializer


# GET: qualquer um
# POST: só empresas
# PATCH, PUT: só empresa dona da vaga
# Para encontrar dados de determinada empresa basta acrescentar /id
class VagaViewSet(viewsets.ModelViewSet):
    queryset = models.Vaga.objects.all()
    serializer_class = serializers.VagaSerializer


    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return permissions.AllowAny()
    #
    #     if self.request.method == 'POST':
    #         return permissions.AllowAny()
    #
    #     return permissions.IsAuthenticated(), IsOwner()
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         Usuario.objects.create_user(**serializer.validated_data)
    #
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    #
    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Usuário não pode ser criado com dados recebidos.'
    #     }, status=status.HTTP_400_BAD_REQUEST)

# class ListCourses(APIView):
#     def get(self, request, format=None):
#         course = [Course.name for Course in Course.objects.all()]
#         return Response(course)
#
#
# class SearchVacancy(APIView):
#     def get(self, request, format=None):
#         vacancy = VacantJob.objects.all()
#
#         # Parametro icreated: data de insercao minima (deve ser passada no formato YYYYMM)
#         if 'icreated' in request.GET:
#             try:
#                 # Transforma parametro em objeto datetime para ser usado no filtro
#                 creationDate = datetime.datetime.strptime(request.GET.get('icreated'), '%Y%m')
#             except ValueError:
#                 return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")
#
#             vacancy = vacancy.filter(created_at__date__gte=creationDate)
#
#         # Parametro fcreated: data de insercao maxima (deve ser passada no formato YYYYMM)
#         if 'fcreated' in request.GET:
#             try:
#                 # Transforma parametro em objeto datetime para ser usado no filtro
#                 creationDate = datetime.datetime.strptime(request.GET.get('fcreated'), '%Y%m')
#             except ValueError:
#                 return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")
#
#             vacancy = vacancy.filter(created_at__date__lte=creationDate)
#
#         # Parametro course: Curso da vaga (deve ser passada abreviacao do curso)
#         if 'course' in request.GET:
#             courses = [VacantJobHasCourse.vacant_job_id_id for VacantJobHasCourse in
#                        VacantJobHasCourse.objects.all().filter(course_id__abbreviation=request.GET.get('course'))]
#             vacancy = vacancy.filter(id_vacancy__in=courses)
#
#         # Parametro company: Nome da empresa que oferece a vaga
#         if 'company' in request.GET:
#             companies = [Hiring.id_vacancy_id for Hiring in
#                          Hiring.objects.filter(id_company__name__icontains=request.GET.get('company'))]
#             vacancy = vacancy.filter(id_vacancy__in=companies)
#
#         vacancy = [VacantJob.role for VacantJob in vacancy]
#
#         return Response(vacancy)
#
#


# User = get_user_model()

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permissions_classes = [AllowAny]


# class CompanyCreateAPIView(CreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#
# class CompanyListAPIView(ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
#
# class StudentCreateAPIView(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentListAPIView(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailAPIView(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class UserListAPIView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.UserSerializer
#     queryset = models.User.objects.all()


# class ExampleView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     renderer_classes = (JSONRenderer,)
#
#     def get(self, request, format=None):
#         content = {'nome': 'mateus'}
#         return Response(content)
#
#         # LOGOUT
#         # def get(self, request, format=None):
#         #     # simply delete the token to force a login
#         #     request.user.auth_token.delete()
#         #     return Response(status=status.HTTP_200_OK)
