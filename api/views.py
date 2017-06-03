# from django.core.validators import validate_email
# from django.http import HttpResponse, Http404, JsonResponse
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Lista Todos os cursos presentes na base de dados
# class ListCourses(APIView):
#     def get(self, request, format=None):
#         course = [Course.name for Course in Course.objects.all()]
#         return Response(course)
#
# # Lista Todas as empresas presentes na base de dados
# class ListCompanies(APIView):
#     def get(self, request, format=None):
#         companies = [Company.name for Company in Company.objects.all()]
#         return Response(companies)
#
# #Busca se uma determinada empresa existe na base de dados
# class SearchCompany(APIView):
#     def get(self, request, name=None):
#         #Parametro name: Nome da Empresa
#         try:
#             company = [Company.name for Company in Company.objects.filter(name=name)]
#         except Company.DoesNotExist:
#             company = None
#
#         return Response(company)
#
# #A empresa logada pode listar as vagas de estagio que criou
# class SearchOpportunity(APIView):
#     def get(self, request, id=None):
#         #Parametro id: id de ususario da empresa
#         cnpj = list(Company.objects.filter(iduser=id))
#         if not cnpj:
#             raise Http404("User does not exist.")
#
#         try:
#             company = [Company.cnpj for Company in Company.objects.filter(iduser=id)]
#         except ValueError:
#                 return Response("Nao e um usuario")
#
#         try:
#             vacancy_id = [Hiring.id_vacancy_id for Hiring in Hiring.objects.filter(id_company_id=company[0])]
#         except Hiring.DoesNotExist:
#             vacancy_id = None
#
#         try:
#             vacant_job_name = [VacantJob.role  for VacantJob in VacantJob.objects.filter(id_vacancy=vacancy_id[0])]
#         except VacantJob.DoesNotExist:
#             vacant_job_name = None
#
#         return Response(vacant_job_name)
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


# User = get_user_model()

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permissions_classes = [AllowAny]


# from .serializers import UserSerializer, StudentSerializer, CompanySerializer

# from api.models import (
#     # Company,
#     # Course,
#     # Curriculum,
#     # Hiring,
#     # Student,
#     # VacantJob,
#     # VacantJobHasCourse,
#     # User,
# )

# import datetime

from rest_framework import viewsets, filters
from api import models, serializers, permissions

# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email',)

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
# class SearchCompany(APIView):
#     def get(self, request, format=None):
#
#         if 'id' in request.GET:
#             info = list(Student.objects.filter(user=request.GET.get('id')))
#             if not info:
#                 raise Http404("User does not exist.")
#
#             try:
#                 cpf = [Student.cpf for Student in Student.objects.filter(user=request.GET.get('id'))]
#             except Student.DoesNotExist:
#                 cpf = None
#
#             try:
#                 curriculum_info = [Curriculum.course_id_id for Curriculum in Curriculum.objects.filter(cpf_id=cpf[0])]
#             except Curriculum.DoesNotExist:
#                 curriculum_info = None
#
#             try:
#                 vacant_job_info = [VacantJobHasCourse.vacant_job_id_id for VacantJobHasCourse in
#                                    VacantJobHasCourse.objects.all().filter(course_id_id=curriculum_info[0])]
#             except Curriculum.DoesNotExist:
#                 vacant_job_info = None
#
#             companies_cnpj = []
#             for vacant_job in vacant_job_info:
#                 try:
#                     sql_companies_id = [Hiring.id_company_id for Hiring in
#                                         Hiring.objects.filter(id_vacancy_id=vacant_job)]
#                     for sql_company_id in sql_companies_id:
#                         companies_cnpj.append(sql_company_id)
#                 except Curriculum.DoesNotExist:
#                     sql_companies_id = None
#
#             companies_name = []
#             for company_id in companies_cnpj:
#                 try:
#                     sql_companies_name = [Company.name for Company in Company.objects.filter(cnpj=company_id)]
#                     for sql_company_name in sql_companies_name:
#                         companies_name.append(sql_company_name)
#                 except Company.DoesNotExist:
#                     sql_companies_name = None
#
#             return Response(companies_name)
#
#         elif 'name' in request.GET:
#             company_name = list(Company.objects.filter(name=request.GET.get('name')))
#             if not company_name:
#                 raise Http404("Company does not exist.")
#
#             company = [Company.name for Company in Company.objects.filter(name=request.GET.get('name'))]
#             return Response(company)
#         else:
#             companies = [Company.name for Company in Company.objects.all()]
#             return Response(companies)
#
#
# class SearchOpportunity(APIView):
#     def get(self, request, id=None):
#
#         if 'id' in request.GET:
#
#             cpf = list(Student.objects.filter(user=request.GET.get('id')))
#             if not cpf:
#                 raise Http404("Opportunity does not exist.")
#
#             try:
#                 curriculum_info = [Curriculum.course_id_id for Curriculum in Curriculum.objects.filter(cpf_id=cpf[0])]
#             except Curriculum.DoesNotExist:
#                 curriculum_info = None
#
#             try:
#                 vacant_job_info = [VacantJobHasCourse.vacant_job_id_id for VacantJobHasCourse in
#                                    VacantJobHasCourse.objects.all().filter(course_id_id=curriculum_info[0])]
#             except Curriculum.DoesNotExist:
#                 vacant_job_info = None
#
#             oportunity_name = []
#             for vacant_job in vacant_job_info:
#                 try:
#                     oportunity = [VacantJob.role for VacantJob in VacantJob.objects.filter(id_vacancy=vacant_job)]
#                     for name in oportunity:
#                         oportunity_name.append(oportunity)
#                 except Curriculum.DoesNotExist:
#                     oportunity = None
#
#             return Response(oportunity_name)


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
