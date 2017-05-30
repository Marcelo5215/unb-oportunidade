from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Address(models.Model):
    id_address = models.AutoField(primary_key=True)
    city = models.CharField(max_length=45)
    neighborhood = models.CharField(max_length=45)
    number = models.CharField(max_length=4)
    complement = models.CharField(max_length=45)
    zip_code = models.CharField(max_length=8)
    public_place = models.CharField(max_length=45)

    class Meta:
        db_table = 'Address'

    def __unicode__(self):
        return '{}'.format(self.id_address)

class Student(models.Model):
    cpf = models.CharField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{11}$')])
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    id_user = models.ForeignKey(User, unique=True)
    phone_number = models.CharField(max_length=45)
    regular_student = models.BooleanField()

    class Meta:
        db_table = 'students'

    def __unicode__(self):
        return '[{}] {}'.format(self.id_user, self.cpf)

class BankNames(models.Model):
    bank_number = models.IntegerField(primary_key=True)
    bank_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Bank_names'

    def __unicode__(self):
        return self.bank_number

class BankAccounts(models.Model):
    id_bank_accounts = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=20)
    agency_number = models.CharField(max_length=10)
    bank_names_bank_number = models.ForeignKey(BankNames)
    student_cpf = models.ForeignKey(Student)

    class Meta:
        db_table = 'Bank_accounts'

    def __unicode__(self):
        return '{} [{}] [{}]'.format(self.id_bank_accounts, self.bank_names_bank_number, self.student_cpf)


class Company(models.Model):
    cnpj = models.AutoField(primary_key=True, max_length=14, validators=[RegexValidator(r'^\d{14}$')])
    name = models.CharField(max_length=45)
    corporate_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    address_id = models.ForeignKey(Address)
    id_user = models.ForeignKey(User, unique=True)
    phone_number = models.CharField(max_length=45)
    agreement = models.BooleanField()

    class Meta:
        db_table = 'Companies'

    def __unicode__(self):
        return '{} [{}]'.format(self.cnpj, self.address_id)


class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    class Meta:
        db_table = 'Courses'

    def __unicode__(self):
        return '{}'.format(self.id_course)

class File(models.Model):
    file_name = models.CharField(max_length=500)
    file_path = models.CharField(max_length=500)

class Curriculum(models.Model):
    cpf = models.ForeignKey(Student, primary_key=True)
    time_desired = models.IntegerField()
    work_shift = models.CharField(max_length=20)
    file_id = models.ForeignKey(File)
    university = models.CharField(max_length=45)
    additional_info = models.CharField(max_length=900)
    semester = models.IntegerField()
    course_id = models.ForeignKey(Course)

    class Meta:
        db_table = 'Curriculum'

    def __unicode__(self):
        return '[{}] [{}] {}'.format(self.cpf, self.course_id, self.file_id)

class VacantJob(models.Model):
    id_vacancy = models.AutoField(primary_key=True)
    role = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        db_table = 'Vacant_jobs'

    def __unicode__(self):
        return '{}'.format(self.id_vacancy)


class VacantJobHasCourse(models.Model):
    vacant_job_id = models.ForeignKey(Student, primary_key=True)
    course_id = models.ForeignKey(Course)

    class Meta:
        db_table = 'Vacant_job_has_course'

    def __unicode__(self):
        return '[{}] [{}]'.format(self.vacant_job_id, self.course_id)

class Hiring(models.Model):
    id_hiring = models.AutoField(primary_key=True, )
    contracted_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    contract_end = models.DateTimeField(auto_now_add=True, auto_now=False)
    active = models.BooleanField()
    id_student = models.ForeignKey(Student)
    id_company = models.ForeignKey(Company)
    id_vacancy = models.ForeignKey(VacantJob)

    class Meta:
        db_table = 'Hiring'

    def __unicode__(self):
        return '[{}] [{}] [{}] {}'.format(self.id_student, self.id_company, self.id_vacancy, self.id_hiring)

class Phone(models.Model):
    id_phone = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'Phone'

    def __unicode__(self):
        return '{}'.format(self.phone)


class Requirements(models.Model):
    id_requirements = models.AutoField(primary_key=True)
    work_shift = models.CharField(max_length=20)
    workload = models.IntegerField()
    additional_info = models.CharField(max_length=500)
    minimum_period = models.IntegerField()

    class Meta:
        db_table = 'Requirements'

    def __unicode__(self):
        return '{}'.format(self.id_requirements)


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    destiny = models.IntegerField()
    stars = models.IntegerField()
    feedback = models.CharField(max_length=500)
    cnpj_company = models.ForeignKey(Company)
    hiring_id = models.ForeignKey(Hiring)

    class Meta:
        db_table = 'Reviews'

    def __unicode__(self):
        return '{} [{}] [{}]'.format(self.id_review, self.cnpj_company, self.hiring_id)
