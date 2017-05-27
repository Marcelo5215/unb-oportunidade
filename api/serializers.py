from rest_framework import models

from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Company
from api.models import Address
from api.models import Phone


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields = ('id', 'email', 'password')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        # fields = ('city', 'neighborhood', 'number', 'complement', 'zip_code', 'public_place')


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
        # fields = 'phone'


class CompanySerializer(serializers.ModelSerializer):
    company_user = UserSerializer()
    company_address = AddressSerializer()
    company_phone = PhoneSerializer()

    class Meta:
        model = Company
        fields = ('company_user', 'cnpj', 'name',
                  'corporate_name', 'phone_number', 'company_address', 'company_phone')
        read_only_fields = ('created_at', 'updated_at')
