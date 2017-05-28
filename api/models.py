# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    public_place = models.CharField(db_column='public place', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number = models.CharField(max_length=4, blank=False, null=False)
    complement = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Advisor(models.Model):
    advisor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    curso = models.ForeignKey('Course', models.DO_NOTHING, db_column='curso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advisor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BankAccounts(models.Model):
    idbank_accounts = models.IntegerField(primary_key=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    agency_number = models.CharField(max_length=10, blank=True, null=True)
    bank_names_bank_number = models.ForeignKey('BankNames', models.DO_NOTHING, db_column='bank_names_bank_number')
    student_cpf = models.ForeignKey('Student', models.DO_NOTHING, db_column='student_cpf')

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class BankNames(models.Model):
    bank_number = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_names'


class Company(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.IntegerField(primary_key=True)
    corporate_name = models.CharField(max_length=45, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='address', blank=True, null=True)
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    agreement = models.IntegerField(blank=True, null=True)
    intermediate = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyHasPhone(models.Model):
    company_cnpj = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_cnpj', primary_key=True)
    phone = models.ForeignKey('Phone', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'company_has_phone'
        unique_together = (('company_cnpj', 'phone'),)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    cpf = models.ForeignKey('Student', models.DO_NOTHING, db_column='cpf', primary_key=True)
    time_desired = models.IntegerField(blank=True, null=True)
    work_shift = models.CharField(max_length=20, blank=True, null=True)
    file = models.ForeignKey('File', models.DO_NOTHING, blank=True, null=True)
    university = models.CharField(max_length=45, blank=True, null=True)
    aditional_info = models.CharField(max_length=900, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curriculum'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class File(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=500, blank=True, null=True)
    filepath = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'


class Hiring(models.Model):
    id_hiring = models.IntegerField(primary_key=True)
    contractedat = models.DateTimeField(db_column='contractedAt', blank=True, null=True)  # Field name made lowercase.
    contratactend = models.DateTimeField(db_column='contratactEnd', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    id_student = models.ForeignKey('Student', models.DO_NOTHING, db_column='id_student', blank=True, null=True)
    id_company = models.ForeignKey(Company, models.DO_NOTHING, db_column='id_company', blank=True, null=True)
    id_vacant_job = models.ForeignKey('VacantJob', models.DO_NOTHING, db_column='id_vacant_job', blank=True, null=True)
    additive_first = models.DateTimeField(blank=True, null=True)
    additive_second = models.DateTimeField(blank=True, null=True)
    additive_third = models.DateTimeField(blank=True, null=True)
    additive_fourth = models.DateTimeField(blank=True, null=True)
    document_enter = models.DateTimeField(blank=True, null=True)
    advisor_first = models.ForeignKey(Advisor, models.DO_NOTHING, db_column='advisor_first', blank=True, null=True, related_name='%(class)s_advisor_first')
    advisor_second = models.ForeignKey(Advisor, models.DO_NOTHING, db_column='advisor_second', blank=True, null=True, related_name='%(class)s_advisor_second')
    broken_contract = models.DateTimeField(blank=True, null=True)
    document_left = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hiring'


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone'


class Requirement(models.Model):
    id = models.IntegerField(primary_key=True)
    workload = models.IntegerField(blank=True, null=True)
    work_shift = models.CharField(max_length=20, blank=True, null=True)
    additional_information = models.CharField(max_length=500, blank=True, null=True)
    minimun_period = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    destiny = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    company_cnpj = models.ForeignKey(Company, models.DO_NOTHING, db_column='company_cnpj', blank=True, null=True)
    hiring = models.ForeignKey(Hiring, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class Student(models.Model):
    cpf = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.EmailField()  
    full_name = models.CharField(max_length=200, blank=True, null=True)
    regular_student = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Address, models.DO_NOTHING, blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='course', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentHasPhone(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, primary_key=True)
    phone = models.ForeignKey(Phone, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student_has_phone'
        unique_together = (('student', 'phone'),)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    tp_user = models.ForeignKey(Role, models.DO_NOTHING, db_column='tp_user', blank=True, null=True)
    #student_cpf = models.ForeignKey(Student, models.DO_NOTHING, db_column='student_cpf')

    class Meta:
        managed = False
        db_table = 'user'


class VacantJob(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vacant_job'


class VacantJobHasCourse(models.Model):
    vacant_job = models.ForeignKey(VacantJob, models.DO_NOTHING, primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vacant_job_has_course'
        unique_together = (('vacant_job', 'course'),)


class VacantJobHasRequirement(models.Model):
    vacant_job = models.ForeignKey(VacantJob, models.DO_NOTHING, primary_key=True)
    requirement = models.ForeignKey(Requirement, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vacant_job_has_requirement'
        unique_together = (('vacant_job', 'requirement'),)
