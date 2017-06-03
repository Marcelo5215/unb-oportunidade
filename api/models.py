# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


# class Address(models.Model):
#     id = models.IntegerField(primary_key=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     neighborhood = models.CharField(max_length=100, blank=True, null=True)
#     public_place = models.CharField(db_column='public place', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
#     number = models.CharField(max_length=4, blank=False, null=False)
#     complement = models.CharField(max_length=100, blank=True, null=True)
#     cep = models.CharField(max_length=8, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'address'
#
#
# class Advisor(models.Model):
#     advisor_id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     curso = models.ForeignKey('Course', models.DO_NOTHING, db_column='curso', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'advisor'


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class BankAccounts(models.Model):
#     idbank_accounts = models.IntegerField(primary_key=True)
#     account_number = models.CharField(max_length=20, blank=True, null=True)
#     agency_number = models.CharField(max_length=10, blank=True, null=True)
#     bank_names_bank_number = models.ForeignKey('BankNames', models.DO_NOTHING, db_column='bank_names_bank_number')
#     student_cpf = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_cpf')
#
#     class Meta:
#         managed = False
#         db_table = 'bank_accounts'
#
#
# class BankNames(models.Model):
#     bank_number = models.IntegerField(primary_key=True)
#     bank_name = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bank_names'
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=45, blank=True, null=True)
#     cnpj = models.IntegerField(primary_key=True)
#     corporate_name = models.CharField(max_length=45, blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
#     address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address', blank=True, null=True)
#     iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
#     agreement = models.IntegerField(blank=True, null=True)
#     intermediate = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'company'
#
#
# class CompanyHasPhone(models.Model):
#     company_cnpj = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_cnpj', primary_key=True)
#     phone = models.ForeignKey('Phone', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'company_has_phone'
#         unique_together = (('company_cnpj', 'phone'),)
#
#
# class Course(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     abbreviation = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'course'
#
#
# class Curriculum(models.Model):
#     cpf = models.ForeignKey('Student', models.DO_NOTHING, db_column='cpf', primary_key=True)
#     time_desired = models.IntegerField(blank=True, null=True)
#     work_shift = models.CharField(max_length=20, blank=True, null=True)
#     file = models.ForeignKey('File', models.DO_NOTHING, blank=True, null=True)
#     university = models.CharField(max_length=45, blank=True, null=True)
#     aditional_info = models.CharField(max_length=900, blank=True, null=True)
#     semester = models.IntegerField(blank=True, null=True)
#     course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'curriculum'
#
#
# class File(models.Model):
#     id = models.IntegerField(primary_key=True)
#     filename = models.CharField(max_length=500, blank=True, null=True)
#     filepath = models.CharField(max_length=500, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'file'
#
#
# class Hiring(models.Model):
#     id_hiring = models.IntegerField(primary_key=True)
#     contractedat = models.DateTimeField(db_column='contractedAt', blank=True, null=True)  # Field name made lowercase.
#     contratactend = models.DateTimeField(db_column='contratactEnd', blank=True, null=True)  # Field name made lowercase.
#     active = models.IntegerField(blank=True, null=True)
#     id_student = models.ForeignKey('Student', models.DO_NOTHING, db_column='id_student', blank=True, null=True)
#     id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company', blank=True, null=True)
#     id_vacant_job = models.ForeignKey('VacantJob', models.DO_NOTHING, db_column='id_vacant_job', blank=True, null=True)
#     additive_first = models.DateTimeField(blank=True, null=True)
#     additive_second = models.DateTimeField(blank=True, null=True)
#     additive_third = models.DateTimeField(blank=True, null=True)
#     additive_fourth = models.DateTimeField(blank=True, null=True)
#     document_enter = models.DateTimeField(blank=True, null=True)
#     advisor_first = models.ForeignKey(Advisor, models.DO_NOTHING, db_column='advisor_first', blank=True, null=True, related_name='%(class)s_advisor_first')
#     advisor_second = models.ForeignKey(Advisor, models.DO_NOTHING, db_column='advisor_second', blank=True, null=True, related_name='%(class)s_advisor_second')
#     broken_contract = models.DateTimeField(blank=True, null=True)
#     document_left = models.DateTimeField(blank=True, null=True)
#     comments = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hiring'
#
#
# class Phone(models.Model):
#     id = models.IntegerField(primary_key=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'phone'
#
#
# class Requirement(models.Model):
#     id = models.IntegerField(primary_key=True)
#     workload = models.IntegerField(blank=True, null=True)
#     work_shift = models.CharField(max_length=20, blank=True, null=True)
#     additional_information = models.CharField(max_length=500, blank=True, null=True)
#     minimun_period = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'requirement'
#
#
# class Review(models.Model):
#     id = models.IntegerField(primary_key=True)
#     destiny = models.IntegerField(blank=True, null=True)
#     stars = models.IntegerField(blank=True, null=True)
#     feedback = models.CharField(max_length=500, blank=True, null=True)
#     company_cnpj = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_cnpj', blank=True, null=True)
#     hiring = models.ForeignKey(Hiring, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'review'


# class Role(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     label = models.CharField(max_length=45)
#
#     class Meta:
#         # managed = False
#         db_table = 'role'
#
#     def __str__(self):
#         return self.label


# class Student(models.Model):
#     cpf = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=45, blank=True, null=True)
#     email = models.EmailField()
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     regular_student = models.IntegerField(blank=True, null=True)
#     address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
#     registration_number = models.CharField(max_length=20, blank=True, null=True)
#     course = models.ForeignKey(Course, models.DO_NOTHING, db_column='course', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'student'
#
#
# class StudentHasPhone(models.Model):
#     student = models.ForeignKey(Student, models.DO_NOTHING, primary_key=True)
#     phone = models.ForeignKey(Phone, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'student_has_phone'
#         unique_together = (('student', 'phone'),)


class Arquivo(models.Model):
    nome_arquivo = models.CharField(max_length=255, unique=True, blank=False)
    path_arquivo = models.CharField(max_length=255, unique=True, blank=False)


class Banco(models.Model):
    nome = models.CharField(max_length=100, unique=True, blank=False)


class ContaBancaria(models.Model):
    numero_conta = models.IntegerField(null=False)
    numero_agencia = models.IntegerField(null=False)
    banco = models.ForeignKey('Banco', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'conta_bancaria'
        verbose_name = 'Conta Bancária'
        verbose_name_plural = 'Contas Bancárias'


class Curso(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    sigla = models.CharField(max_length=10, blank=False)


class CV(models.Model):
    info_adicional = models.TextField(max_length=500)
    arquivo = models.OneToOneField('Arquivo', on_delete=models.CASCADE)
    turno = models.OneToOneField('Turno', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Currículo'
        verbose_name_plural = 'Currículos'


class Empresa(models.Model):
    cnpj = models.IntegerField(primary_key=True, auto_created=False)
    nome = models.CharField(max_length=100, blank=False)
    nome_fantasia = models.CharField(max_length=100, blank=False)
    conveniada = models.BooleanField(default=True, null=False)
    usuario = models.OneToOneField('Usuario', on_delete=models.CASCADE)


class Endereco(models.Model):
    endereço = models.CharField(max_length=100, blank=False)
    bairro = models.CharField(max_length=25, blank=False)
    numero = models.CharField(max_length=5, blank=False, validators=[RegexValidator(r'^\d$')])
    complemento = models.CharField(max_length=25, blank=True)
    cidade = models.CharField(max_length=50, blank=False)
    cep = models.CharField(max_length=8, blank=False, validators=[RegexValidator(r'^\d{8}$')])
    usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Estudante(models.Model):
    cpf = models.IntegerField(primary_key=True, auto_created=False)
    nome_completo = models.CharField(max_length=255, blank=False)
    estudante_regular = models.BooleanField(null=False)
    matricula = models.CharField(max_length=9, validators=[RegexValidator(r'^d{9}$'),], blank=False)
    semestre = models.IntegerField(null=False)
    universidade = models.CharField(max_length=45, blank=False)
    curso = models.ForeignKey('Curso', on_delete=models.DO_NOTHING)


class Telefone(models.Model):
    numero_telefone = models.CharField(max_length=9, blank=False)
    usuario = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING)


class Turno(models.Model):
    turno = models.CharField(max_length=20, blank=False)


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
    is_estudante = models.BooleanField(null=False)
    is_empresa = models.BooleanField(null=False)
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


# class VacantJob(models.Model):
#     id = models.IntegerField(primary_key=True)
#     role = models.CharField(max_length=200, blank=True, null=True)
#     createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
#     updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'vacant_job'
#
#
# class VacantJobHasCourse(models.Model):
#     vacant_job = models.ForeignKey(VacantJob, models.DO_NOTHING, primary_key=True)
#     course = models.ForeignKey(Course, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'vacant_job_has_course'
#         unique_together = (('vacant_job', 'course'),)
#
#
# class VacantJobHasRequirement(models.Model):
#     vacant_job = models.ForeignKey(VacantJob, models.DO_NOTHING, primary_key=True)
#     requirement = models.ForeignKey(Requirement, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'vacant_job_has_requirement'
#         unique_together = (('vacant_job', 'requirement'),)
