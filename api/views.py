from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.


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
