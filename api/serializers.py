from api.models import Company, Address, Phone, Student

from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('email', 'password', 'tp_user')


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
    # company_user = UserSerializer()
    company_address = AddressSerializer()
    company_phone = PhoneSerializer()

    class Meta:
        model = Company
        fields = ('cnpj', 'name',
                  'corporate_name', 'company_address', 'company_phone')
        read_only_fields = ('created_at', 'updated_at')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('cpf', 'first_name', 'email',
                  'full_name', 'regular_student', 'registration_number')