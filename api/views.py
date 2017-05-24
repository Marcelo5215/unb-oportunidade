from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Company
from api.models import Course
from api.models import Vacant_job

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
