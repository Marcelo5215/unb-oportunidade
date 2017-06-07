from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from . import models


class UsuarioSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = models.Usuario
        fields = ('id', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def create(self, validated_data):

        user = models.Usuario(email=validated_data['email'])

        if validated_data['password'] != validated_data['confirm_password']:
            raise ValueError('Senha e confirmação não conferem.')

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()
        elif password != confirm_password:
            raise ValueError('Senha e confirmação não conferem.')

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
