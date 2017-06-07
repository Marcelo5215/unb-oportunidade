from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


def caminho_imagem_empresa(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'media/user_{0}/{1}'.format(instance.usuario_id, filename)


def caminho_arquivo_estudante(instance, filename):
    return 'files/vaga_{0}/{1}_{2}'.format(instance.vaga_id, instance.email, filename)


class ContratoInfo(models.Model):
    nome = models.CharField(verbose_name='Nome do aluno', max_length=255, blank=False)
    matricula = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{9}$')], unique=True, blank=False)
    inicio_contrato = models.DateField(null=False)
    fim_contrato = models.DateField(null=False)
    is_ativo = models.BooleanField(verbose_name='está ativo?', null=False)
    aditivo_primeiro = models.DateField(null=True, blank=True)
    aditivo_segundo = models.DateField(null=True, blank=True)
    aditivo_terceiro = models.DateField(null=True, blank=True)
    aditivo_quarto = models.DateField(null=True, blank=True)
    orientador_um = models.CharField(max_length=100)
    orientador_dois = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Aluno: ' + self.nome + ' | Matrícula: ' + self.matricula + ' | Início do Contrato: ' + self.inicio_contrato.__str__() + ' | Fim do Contrato: ' + self.fim_contrato.__str__()

    class Meta:
        db_table = 'contrato_info'
        verbose_name = 'Informações do Contrato'
        verbose_name_plural = 'Informações dos Contratos'


class Curso(models.Model):
    nome = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Empresa(models.Model):
    cnpj = models.IntegerField(primary_key=True, auto_created=False)
    razao_social = models.CharField(max_length=100, blank=False)
    nome_fantasia = models.CharField(max_length=100, blank=False)
    conveniada = models.BooleanField(verbose_name='é conveniada com a UnB?',default=True, null=False)
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=caminho_imagem_empresa, default='media/unb.jpg')

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class InteresseEmVaga(models.Model):
    vaga = models.ForeignKey('Vaga', on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100, blank=False)
    matricula = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{9}$')], blank=False)
    semestre = models.IntegerField(null=False)
    CV = models.FileField(null=False, upload_to=caminho_arquivo_estudante)
    email = models.EmailField(blank=False)
    telefone = models.CharField(verbose_name='(xx) xxxxx-xxxx', max_length=11, validators=[RegexValidator(r'^\d{11}$')], blank=False)

    def __str__(self):
        return self.nome_completo

    class Meta:
        db_table = 'interesse_em_vaga'
        verbose_name = 'Interesse em Vaga'
        verbose_name_plural = 'Interesses em Vagas'
        unique_together = (('vaga', 'email'),)


class Turno(models.Model):
    turno = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.turno

    class Meta:
        db_table = 'turno'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Usuários devem ter um email válido.')

        email = self.normalize_email(email)
        usuario = self.model(email=email)

        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password):

        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class Vaga(models.Model):
    atualizada_em = models.DateTimeField(auto_now=True)
    carga_horaria = models.IntegerField(null=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    curso = models.ManyToManyField('Curso')
    descricao = models.TextField(max_length=500, blank=False)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    is_ativa = models.BooleanField(verbose_name='está ativa?', null=False)
    semestre_minimo = models.IntegerField(null=False)
    titulo = models.CharField(max_length=100, blank=False)
    turno = models.OneToOneField('Turno', on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'vaga'
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
