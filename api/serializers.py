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
        fields = ('cnpj', 'razao_social', 'nome_fantasia', 'usuario', 'imagem')


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
