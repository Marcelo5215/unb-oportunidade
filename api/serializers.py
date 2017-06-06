# from api.models import Company, Address, Phone, Student

from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from . import models


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = ('id', 'email', 'password', 'is_estudante', 'is_empresa')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = models.Usuario(
            email=validated_data['email'],
            is_estudante=validated_data['is_estudante'],
            is_empresa=validated_data['is_empresa']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.is_empresa = validated_data.get('is_empresa', instance.is_empresa)
        instance.is_estudante = validated_data.get('is_estudante', instance.is_estudante)

        instance.save()

        password = validated_data.get('password', None)

        if password:
            instance.set_password(password)
            instance.save()

        update_session_auth_hash(self.context.get('request'), instance)

        return instance


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Curso
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Empresa
        fields = '__all__'


class InteresseEmVagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.InteresseEmVaga
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Turno
        fields = '__all__'


class VagaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vaga
        fields = '__all__'


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'
#         # fields = ('city', 'neighborhood', 'number', 'complement', 'zip_code', 'public_place')
#
#
# class PhoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = 'phone'
#
#
# class CompanySerializer(serializers.ModelSerializer):
#     # company_user = UserSerializer()
#     company_address = AddressSerializer()
#     company_phone = PhoneSerializer()
#
#     class Meta:
#         model = Company
#         fields = ('cnpj', 'name',
#                   'corporate_name', 'company_address', 'company_phone')
#         read_only_fields = ('created_at', 'updated_at')
#
#
# class StudentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Student
#         fields = ('cpf', 'first_name', 'email',
#                   'full_name', 'regular_student', 'registration_number')
