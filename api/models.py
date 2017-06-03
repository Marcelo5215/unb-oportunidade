from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Avaliacao(models.Model):
    nota = models.IntegerField(null=False, validators=[MaxValueValidator(10), MinValueValidator(1)])
    feedback = models.TextField(max_length=500, blank=True)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    class Meta:
        db_table = 'avaliacao'
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'


class Arquivo(models.Model):
    nome_arquivo = models.CharField(max_length=255, unique=True, blank=False)
    path_arquivo = models.CharField(max_length=255, unique=True, blank=False)

    class Meta:
        db_table = 'arquivo'
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'


class Banco(models.Model):
    nome = models.CharField(max_length=100, unique=True, blank=False)

    class Meta:
        db_table = 'banco'
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'


class ContaBancaria(models.Model):
    numero_conta = models.IntegerField(null=False)
    numero_agencia = models.IntegerField(null=False)
    banco = models.ForeignKey('Banco', on_delete=models.PROTECT)

    class Meta:
        db_table = 'conta_bancaria'
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'


class ContratoInfo(models.Model):
    inicio_contrato = models.DateTimeField(null=False)
    fim_contrato = models.DateTimeField(null=False)
    is_ativo = models.BooleanField(verbose_name='está ativo?', null=False)
    aditivo_primeiro = models.DateTimeField()
    aditivo_segundo = models.DateTimeField()
    aditivo_terceiro = models.DateTimeField()
    aditivo_quarto = models.DateTimeField()
    orientador_um = models.CharField(max_length=100)
    orientador_dois = models.CharField(max_length=100)
    vaga = models.ForeignKey('Vaga', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contrato_info'
        verbose_name = 'Informações do Contrato'
        verbose_name_plural = 'Informações dos Contratos'


class Curso(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sigla = models.CharField(max_length=10, blank=False)

    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class CV(models.Model):
    info_adicional = models.TextField(max_length=500)
    arquivo = models.OneToOneField('Arquivo', on_delete=models.PROTECT)
    turno = models.OneToOneField('Turno', on_delete=models.PROTECT)

    class Meta:
        db_table = 'cv'
        verbose_name = 'Currículo'
        verbose_name_plural = 'Currículos'


class Empresa(models.Model):
    cnpj = models.IntegerField(primary_key=True, auto_created=False)
    nome = models.CharField(max_length=100, blank=False)
    nome_fantasia = models.CharField(max_length=100, blank=False)
    conveniada = models.BooleanField(default=True, null=False)
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Endereco(models.Model):
    endereco = models.CharField(max_length=100, blank=False)
    bairro = models.CharField(max_length=25, blank=False)
    numero = models.CharField(max_length=5, blank=False, validators=[RegexValidator(r'^\d$')])
    complemento = models.CharField(max_length=25, blank=True)
    cidade = models.CharField(max_length=50, blank=False)
    cep = models.CharField(max_length=8, blank=False, validators=[RegexValidator(r'^\d{8}$')])
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Estudante(models.Model):
    cpf = models.IntegerField(primary_key=True, auto_created=False)
    nome_completo = models.CharField(max_length=255, blank=False)
    estudante_regular = models.BooleanField(null=False)
    matricula = models.CharField(max_length=9, validators=[RegexValidator(r'^d{9}$')], blank=False)
    semestre = models.IntegerField(null=False)
    universidade = models.CharField(max_length=45, blank=False)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    class Meta:
        db_table = 'estudante'
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'


class Telefone(models.Model):
    numero_telefone = models.CharField(max_length=9, blank=False)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'telefone'
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'


class Turno(models.Model):
    turno = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = 'turno'
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):

        if not email:
            raise ValueError('Usuários devem ter um email válido.')

        if kwargs.get('is_estudante') is None:
            raise ValueError('É necessário definir se o usuário é estudante ou não.')

        if kwargs.get('is_empresa') is None:
            raise ValueError('É necessário definir se o usuário é empresa ou não.')

        email = self.normalize_email(email)
        usuario = self.model(
            email=email,
            is_empresa=kwargs.get('is_empresa'),
            is_estudante=kwargs.get('is_estudante')
        )

        usuario.set_password(password)
        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, email, password, **kwargs):

        user = self.create_user(email, password, **kwargs)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    is_estudante = models.BooleanField(verbose_name='é aluno?', null=False)
    is_empresa = models.BooleanField(verbose_name='é empresa?', null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_estudante', 'is_empresa']

    def save(self, *args, **kwargs):
        """Salva o usuário e evita que seja empresa e estudante ao mesmo tempo."""

        if self.is_estudante and self.is_empresa:
            raise ValueError('Usuário deve ser estudante ou empresa.')
        super(Usuario, self).save(*args, **kwargs)

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
    titulo = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(max_length=500, blank=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    carga_horaria = models.IntegerField(null=False)
    semestre_minimo = models.IntegerField(null=False)
    estudante = models.OneToOneField('Estudante', on_delete=models.PROTECT)
    empresa = models.ForeignKey('Empresa', on_delete=models.PROTECT)
    turno = models.OneToOneField('Turno', on_delete=models.PROTECT)
    cursos = models.ManyToManyField('Curso', through='VagaTemCurso')

    class Meta:
        db_table = 'vaga'
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'


class VagaTemCurso(models.Model):
    vaga = models.ForeignKey('Vaga', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)

    class Meta:
        db_table = 'vaga_tem_curso'
