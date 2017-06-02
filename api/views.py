from django.core.validators import validate_email
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, StudentSerializer, CompanySerializer

from api.models import (
    Company,
    Course,
    Curriculum,
    Hiring,
    Student,
    VacantJob,
    VacantJobHasCourse,
    User
)

import datetime


# Create your views here.

# Lista Todos os cursos presentes na base de dados
class ListCourses(APIView):
    def get(self, request, format=None):
        course = [Course.name for Course in Course.objects.all()]
        return Response(course)
    
# Lista Todas as empresas presentes na base de dados 
class ListCompanies(APIView):
    def get(self, request, format=None):
        companies = [Company.name for Company in Company.objects.all()]
        return Response(companies)

#Busca se uma determinada empresa existe na base de dados
class SearchCompany(APIView):
    def get(self, request, name=None):
        #Parametro name: Nome da Empresa
        try:  
            company = [Company.name for Company in Company.objects.filter(name=name)]
        except Company.DoesNotExist:
            company = None
                            
        return Response(company)

#A empresa logada pode listar as vagas de estagio que criou
class SearchOpportunity(APIView):
    def get(self, request, id=None):
        #Parametro id: id de ususario da empresa
        cnpj = list(Company.objects.filter(iduser=id))
        if not cnpj:
            raise Http404("User does not exist.")

        try:  
            company = [Company.cnpj for Company in Company.objects.filter(iduser=id)]
        except ValueError:
                return Response("Nao e um usuario")

        try:
            vacancy_id = [Hiring.id_vacancy_id for Hiring in Hiring.objects.filter(id_company_id=company[0])]
        except Hiring.DoesNotExist:
            vacancy_id = None

        try:
            vacant_job_name = [VacantJob.role  for VacantJob in VacantJob.objects.filter(id_vacancy=vacancy_id[0])]
        except VacantJob.DoesNotExist:
            vacant_job_name = None

        return Response(vacant_job_name)

class SearchVacancy(APIView):
    def get(self, request, format=None):
        vacancy = VacantJob.objects.all()

        # Parametro icreated: data de insercao minima (deve ser passada no formato YYYYMM)
        if 'icreated' in request.GET:
            try:
                # Transforma parametro em objeto datetime para ser usado no filtro
                creationDate = datetime.datetime.strptime(request.GET.get('icreated'), '%Y%m')
            except ValueError:
                return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")

            vacancy = vacancy.filter(created_at__date__gte=creationDate)

        # Parametro fcreated: data de insercao maxima (deve ser passada no formato YYYYMM)
        if 'fcreated' in request.GET:
            try:
                # Transforma parametro em objeto datetime para ser usado no filtro
                creationDate = datetime.datetime.strptime(request.GET.get('fcreated'), '%Y%m')
            except ValueError:
                return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")

            vacancy = vacancy.filter(created_at__date__lte=creationDate)

        # Parametro course: Curso da vaga (deve ser passada abreviacao do curso)
        if 'course' in request.GET:
            courses = [VacantJobHasCourse.vacant_job_id_id for VacantJobHasCourse in
                       VacantJobHasCourse.objects.all().filter(course_id__abbreviation=request.GET.get('course'))]
            vacancy = vacancy.filter(id_vacancy__in=courses)

        # Parametro company: Nome da empresa que oferece a vaga
        if 'company' in request.GET:
            companies = [Hiring.id_vacancy_id for Hiring in
                         Hiring.objects.filter(id_company__name__icontains=request.GET.get('company'))]
            vacancy = vacancy.filter(id_vacancy__in=companies)

        vacancy = [VacantJob.role for VacantJob in vacancy]

        return Response(vacancy)


# User = get_user_model()

# class UserCreateAPIView(CreateAPIView):
#     serializer_class = UserCreateSerializer
#     queryset = User.objects.all()
#     permissions_classes = [AllowAny]


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExampleView(APIView):
    permission_classes = (IsAuthenticated,)

    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        content = {'nome': 'mateus'}
        return Response(content)

        # LOGOUT
        # def get(self, request, format=None):
        #     # simply delete the token to force a login
        #     request.user.auth_token.delete()
        #     return Response(status=status.HTTP_200_OK)
