from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Company
from api.models import Course
from api.models import VacantJob
from api.models import Student
from api.models import Curriculum
from api.models import VacantJobHasCourse
from api.models import Hiring

import datetime

# Create your views here.

class ListCourses(APIView):
    def get(self, request, format=None):
        course = [Course.name for Course in Course.objects.all()]
        return Response(course)

class SearchVacancy(APIView):
    def get(self, request, format=None):
        vacancy = VacantJob.objects.all()

        #Parametro icreated: data de insercao minima (deve ser passada no formato YYYYMM)
        if 'icreated' in request.GET:
            try:
                #Transforma parametro em objeto datetime para ser usado no filtro
                creationDate = datetime.datetime.strptime(request.GET.get('icreated'), '%Y%m')
            except ValueError:
                return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")

            vacancy = vacancy.filter(created_at__date__gte = creationDate)

        #Parametro fcreated: data de insercao maxima (deve ser passada no formato YYYYMM)
        if 'fcreated' in request.GET:
            try:
                #Transforma parametro em objeto datetime para ser usado no filtro
                creationDate = datetime.datetime.strptime(request.GET.get('fcreated'), '%Y%m')
            except ValueError:
                return Response("Parametro 'created' nao eh uma data valida no formato YYYYMM")

            vacancy = vacancy.filter(created_at__date__lte = creationDate)

        #Parametro course: Curso da vaga (deve ser passada abreviacao do curso)
        if 'course' in request.GET:
            courses = [VacantJobHasCourse.vacant_job_id_id  for VacantJobHasCourse in VacantJobHasCourse.objects.all().filter(course_id__abbreviation = request.GET.get('course'))]
            vacancy = vacancy.filter(id_vacancy__in = courses)

        #Parametro company: Nome da empresa que oferece a vaga
        if 'company' in request.GET:
            companies = [Hiring.id_vacancy_id  for Hiring in Hiring.objects.filter(id_company__name__icontains = request.GET.get('company'))]
            vacancy = vacancy.filter(id_vacancy__in = companies)

        vacancy = [VacantJob.role for VacantJob in vacancy]

        return Response(vacancy)


class SearchCompany(APIView):
    def get(self, request, format=None):

        if 'id' in request.GET:
            info = list(Student.objects.filter(id_user= request.GET.get('id')))
            if not info:
                raise Http404("Not exist this user.")

            try:
                cpf = [Student.cpf for Student in Student.objects.filter(id_user=request.GET.get('id'))]
            except Student.DoesNotExist:
                cpf = None

            try:
                curriculum_info = [Curriculum.course_id_id for Curriculum in Curriculum.objects.filter(cpf_id=cpf[0])]
            except Curriculum.DoesNotExist:
                curriculum_info = None

            try:
                vacant_job_info = [VacantJobHasCourse.vacant_job_id_id  for VacantJobHasCourse in VacantJobHasCourse.objects.all().filter(course_id_id=curriculum_info[0])]
            except Curriculum.DoesNotExist:
                vacant_job_info = None

            companies_cnpj = []
            for vacant_job in vacant_job_info:
                try:
                    sql_companies_id = [Hiring.id_company_id  for Hiring in Hiring.objects.filter(id_vacancy_id=vacant_job)]
                    for sql_company_id in sql_companies_id:
                        companies_cnpj.append(sql_company_id)
                except Curriculum.DoesNotExist:
                    sql_companies_id = None

            companies_name = []
            for company_id in companies_cnpj:
                try:
                    sql_companies_name = [Company.name for Company in Company.objects.filter(cnpj=company_id)]
                    for sql_company_name in sql_companies_name: 
                        companies_name.append(sql_company_name)
                except Company.DoesNotExist:
                    sql_companies_name = None

            return Response(companies_name)

        elif 'name' in request.GET:
                company_name = list(Company.objects.filter(name=request.GET.get('name')))
                if not  company_name:
                    raise Http404("This company don't exist.")
                
                company = [Company.name for Company in Company.objects.filter(name=request.GET.get('name'))]
                return Response(company)
        else:
                companies = [Company.name for Company in Company.objects.all()]
                return Response(companies)

class SearchOportunity(APIView):
    def get(self, request, id=None):

        if 'id' in request.GET:

            cpf = list(Student.objects.filter(id_user= request.GET.get('id')))
            if not cpf:
                raise Http404("Not exist this user.")

            try:
                curriculum_info = [Curriculum.course_id_id for Curriculum in Curriculum.objects.filter(cpf_id=cpf[0])]
            except Curriculum.DoesNotExist:
                curriculum_info = None

            try:
                vacant_job_info = [VacantJobHasCourse.vacant_job_id_id  for VacantJobHasCourse in VacantJobHasCourse.objects.all().filter(course_id_id=curriculum_info[0])]
            except Curriculum.DoesNotExist:
                vacant_job_info = None

            oportunity_name = []
            for vacant_job in vacant_job_info:
                try:
                    oportunity = [VacantJob.role  for VacantJob in VacantJob.objects.filter(id_vacancy=vacant_job)]
                    for name in oportunity: 
                        oportunity_name.append(oportunity)
                except Curriculum.DoesNotExist:
                    oportunity = None

            return Response(oportunity_name)
        

class ExempleView(APIView):

    permission_classes = (IsAuthenticated, )

    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        content = {'nome': 'mateus'}
        return Response(content)

    # LOGOUT
    # def get(self, request, format=None):
    #     # simply delete the token to force a login
    #     request.user.auth_token.delete()
    #     return Response(status=status.HTTP_200_OK)
