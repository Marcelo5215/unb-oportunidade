"""unb_oportunidade_src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from api.views import (
#      ListCourses,
#      ListCompanies,
#      ListVacantJob,
#      SearchCompany
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    # url(r'^api/busca/ListCourses/$', ListCourses.as_view()),
    # url(r'^api/busca/ListCompanies/$', ListCompanies.as_view()),
    # url(r'^api/busca/ListVacantJob/$', ListVacantJob.as_view()),
    # url(r'^api/busca/SearchCompany/(?P<nome>[\w\- ]+)/$', SearchCompany.as_view()),
]

# # from unb_oportunidade_src.views import IndexView
# # from rest_framework.routers import DefaultRouter
# # from api import views
# # router = DefaultRouter()
# # router.register('user', views.UserViewSet)
#
#
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
#
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^/$', IndexView.as_view()),
#     url(r'^api/students/create/$', StudentCreateAPIView.as_view(), name='create-student'),
#     url(r'^api/companies/create/$', CompanyCreateAPIView.as_view(), name='create-company'),
#     url(r'^api/companies/$', CompanyListAPIView.as_view(), name='companies'),
#     url(r'^api/students/$', StudentListAPIView.as_view(), name='students'),
#     #url(r'^api/students/(?P<cpf>[\w-]+)/$', StudentDetailAPIView.as_view(), name='students'),
#     url(r'^api/exemplo/get/$', ExampleView.as_view()),
#     url(r'^api/busca/ListCourses/$', ListCourses.as_view()),
#     url(r'^api/busca/ListCompanies/$', ListCompanies.as_view()),
#     url(r'^api/busca/SearchCompany/(?P<name>[\w\- ]+)/$', SearchCompany.as_view()),
#     url(r'^api/busca/SearchVacancy/$', SearchVacancy.as_view()),
#     url(r'^api/busca/SearchOpportunity/(\d+)/$', SearchOpportunity.as_view()),
#     url(r'^api/api-token-auth/', obtain_jwt_token),
#     url(r'^api/api-token-verify/', verify_jwt_token),
#     url(r'^api/api-token-refresh/', refresh_jwt_token),
#
# ]
