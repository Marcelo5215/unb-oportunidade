# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    public_place = models.CharField(db_column='public place', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number = models.CharField(max_length=4, blank=True, null=True)
    complement = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)

    class Meta:        
        db_table = 'address'


class Advisor(models.Model):
    advisor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    curso = models.ForeignKey('Course', db_column='curso', blank=True, null=True)

    class Meta:        
        db_table = 'advisor'


class BankAccounts(models.Model):
    idbank_accounts = models.IntegerField(primary_key=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    agency_number = models.CharField(max_length=10, blank=True, null=True)
    bank_names_bank_number = models.ForeignKey('BankNames', db_column='bank_names_bank_number')
    student_cpf = models.ForeignKey('Student', db_column='student_cpf')

    class Meta:        
        db_table = 'bank_accounts'


class BankNames(models.Model):
    bank_number = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:        
        db_table = 'bank_names'


class Company(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    cnpj = models.IntegerField(primary_key=True, max_length=14, validators=[RegexValidator(r'^\d{14}$')])
    corporate_name = models.CharField(max_length=45, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Address, db_column='address', blank=True, null=True)
    iduser = models.ForeignKey('User', db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    agreement = models.IntegerField(blank=True, null=True)
    intermediate = models.CharField(max_length=100, blank=True, null=True)

    class Meta:        
        db_table = 'company'


class CompanyHasPhone(models.Model):
    company_cnpj = models.ForeignKey(Company, db_column='company_cnpj', primary_key=True)
    phone = models.ForeignKey('Phone')

    class Meta:        
        db_table = 'company_has_phone'
        unique_together = (('company_cnpj', 'phone'),)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:        
        db_table = 'course'


class Curriculum(models.Model):
    cpf = models.ForeignKey('Student', db_column='cpf', primary_key=True)
    time_desired = models.IntegerField(blank=True, null=True)
    work_shift = models.CharField(max_length=20, blank=True, null=True)
    file = models.ForeignKey('File', blank=True, null=True)
    university = models.CharField(max_length=45, blank=True, null=True)
    aditional_info = models.CharField(max_length=900, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)

    class Meta:        
        db_table = 'curriculum'


class File(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=500, blank=True, null=True)
    filepath = models.CharField(max_length=500, blank=True, null=True)

    class Meta:        
        db_table = 'file'


class Hiring(models.Model):
    id_hiring = models.IntegerField(primary_key=True)
    contractedat = models.DateTimeField(db_column='contractedAt', blank=True, null=True)  # Field name made lowercase.
    contratactend = models.DateTimeField(db_column='contratactEnd', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    id_student = models.ForeignKey('Student', db_column='id_student', blank=True, null=True)
    id_company = models.ForeignKey(Company, db_column='id_company', blank=True, null=True)
    id_vacant_job = models.ForeignKey('VacantJob', db_column='id_vacant_job', blank=True, null=True)
    additive_first = models.DateTimeField(blank=True, null=True)
    additive_second = models.DateTimeField(blank=True, null=True)
    additive_third = models.DateTimeField(blank=True, null=True)
    additive_fourth = models.DateTimeField(blank=True, null=True)
    document_enter = models.DateTimeField(blank=True, null=True)
    advisor_first = models.ForeignKey(Advisor, db_column='advisor_first', blank=True, null=True, related_name='advisor_first')
    advisor_second = models.ForeignKey(Advisor, db_column='advisor_second', blank=True, null=True)
    broken_contract = models.DateTimeField(blank=True, null=True)
    document_left = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:        
        db_table = 'hiring'


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:        
        db_table = 'phone'


class Requirement(models.Model):
    id = models.IntegerField(primary_key=True)
    workload = models.IntegerField(blank=True, null=True)
    work_shift = models.CharField(max_length=20, blank=True, null=True)
    additional_information = models.CharField(max_length=500, blank=True, null=True)
    minimun_period = models.IntegerField(blank=True, null=True)

    class Meta:        
        db_table = 'requirement'


class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    destiny = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    company_cnpj = models.ForeignKey(Company, db_column='company_cnpj', blank=True, null=True)
    hiring = models.ForeignKey(Hiring, blank=True, null=True)

    class Meta:        
        db_table = 'review'


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=45, blank=True, null=True)

    class Meta:        
        db_table = 'role'


class Student(models.Model):
    cpf = models.IntegerField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    first_name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    regular_student = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey(Address, blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    course = models.ForeignKey(Course, db_column='course', blank=True, null=True)

    class Meta:        
        db_table = 'student'


class StudentHasPhone(models.Model):
    student = models.ForeignKey(Student, primary_key=True)
    phone = models.ForeignKey(Phone)

    class Meta:        
        db_table = 'student_has_phone'
        unique_together = (('student', 'phone'),)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    tp_user = models.ForeignKey(Role, db_column='tp_user', blank=True, null=True)
    student_cpf = models.ForeignKey(Student, db_column='student_cpf')

    class Meta:        
        db_table = 'user'


class VacantJob(models.Model):
    id = models.IntegerField(primary_key=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:        
        db_table = 'vacant_job'


class VacantJobHasCourse(models.Model):
    vacant_job = models.ForeignKey(VacantJob, primary_key=True)
    course = models.ForeignKey(Course)

    class Meta:        
        db_table = 'vacant_job_has_course'
        unique_together = (('vacant_job', 'course'),)


class VacantJobHasRequirement(models.Model):
    vacant_job = models.ForeignKey(VacantJob, primary_key=True)
    requirement = models.ForeignKey(Requirement)

    class Meta:        
        db_table = 'vacant_job_has_requirement'
        unique_together = (('vacant_job', 'requirement'),)
