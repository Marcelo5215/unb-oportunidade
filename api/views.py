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
from api.models import Vacant_job
from api.models import Student
from api.models import Curriculum
from api.models import Vacant_job_has_course
from api.models import Hiring

import datetime

# Create your views here.

class ListCompany(APIView):
    def get(self, request, format=None):
        companies = [Company.name for Company in Company.objects.all()]
        return Response(companies)

class ListCourses(APIView):
    def get(self, request, format=None):
        course = [Course.name for Course in Course.objects.all()]
        return Response(course)

class ListVacants(APIView):
    def get(self, request, format=None):
        vacant = [Vacant_job.role for Vacant_job in Vacant_job.objects.all()]
        return Response(vacant)

class SearchVacancy(APIView):
    def get(self, request, format=None):
        vacancy = Vacant_job.objects.all()

        if 'created' in request.GET:
            try:
                creationDate = datetime.datetime.strptime(request.GET.get('created'), '%Y%m%d')
            except ValueError:
                return Response("Parametro 'created' nao eh uma data valida no formato YYYYMMDD")

            vacancy = vacancy.filter(created_at__date__gte = creationDate)

        if 'course' in request.GET:
            courses = [Vacant_job_has_course.vacant_job_id_id  for Vacant_job_has_course in Vacant_job_has_course.objects.all().filter(course_id__abbreviation = request.GET.get('course'))]
            vacancy = vacancy.filter(id_vacancy__in = courses)

        if 'company' in request.GET:
            companies = [Hiring.id_vacancy_id  for Hiring in Hiring.objects.filter(id_company__name__icontains = request.GET.get('company'))]
            vacancy = vacancy.filter(id_vacancy__in = companies)

        vacancy = [Vacant_job.role for Vacant_job in vacancy]

        return Response(vacancy)

class SearchCompany(APIView):
    def get(self, request, id=None):

        cpf = list(Student.objects.filter(id_user=id))
        if not cpf:
            raise Http404("Not exist this user.")

        try:
            curriculum_info = [Curriculum.course_id_id for Curriculum in Curriculum.objects.filter(cpf_id=cpf[0])]
        except Curriculum.DoesNotExist:
            curriculum_info = None

        try:
            vacant_job_info = [Vacant_job_has_course.vacant_job_id_id  for Vacant_job_has_course in Vacant_job_has_course.objects.all().filter(course_id_id=curriculum_info[0])]
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
