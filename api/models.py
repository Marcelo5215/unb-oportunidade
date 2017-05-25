from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator





class Address(models.Model):
	adress_id = models.AutoField(primary_key=True)
	city = models.CharField(max_length=45)
	neighborhood = models.CharField(max_length=45)
	number = models.CharField(max_length=4)
	complement = models.CharField(max_length=45)
	zip_code = models.CharField(max_length=8)
	public_place = models.CharField(max_length=45)
	class Meta:
		db_table = 'Address'

	def __unicode__(self):
		return '{}'.format(self.address_id)


class Student(models.Model):
	cpf = models.CharField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{11}$')])
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField()
	id_user = models.ForeignKey(User,unique=True)
	phone_number = models.CharField(max_length=45)
	regular_student = models.BooleanField()
	class Meta:
		db_table = 'students'

	def __unicode__(self):
		return '[{}] {}'.format(self.id_user,self.cpf)


class Company(models.Model):
	cnpj = models.AutoField(primary_key=True)
	name = models.CharField(max_length=45)
	corporate_name = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	address_id = models.ForeignKey(Address)
	id_user = models.OneToOneField(User)
	agreement = models.BooleanField()
	class Meta:
		db_table = 'Companies'

	def __unicode__(self):
		return '{} [{}]'.format(self.cnpj,self.address_id)


class Phone(models.Model):
    id_phone = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=15)
    class Meta:
        db_table = 'Phone'
    def __unicode__(self):
        return '{}'.format(self.id_phone)


class Student_has_phone(models.Model):
    student_id = models.ForeignKey(Student)
    phone_id = models.ForeignKey(Phone)
    class Meta:
        unique_together = ('student_id','phone_id')

    def __unicode__(self):
        return '[{}] [{}]'.format(self.student_id, self.phone_id)


class Company_has_phone(models.Model):
    company_id = models.ForeignKey(Company)
    phone_id = models.ForeignKey(Phone)
    class Meta:
        unique_together = ('company_id','phone_id')

    def __unicode__(self):
        return '[{}] [{}]'.format(self.company_id, self.phone_id)


class File(models.Model):
	file_name = models.CharField(max_length=500)
	file_path = models.CharField(max_length=500)


class Course(models.Model):
	id_course = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=10)
	class Meta:
		db_table = 'Courses'

	def __unicode__(self):
		return '{}'.format(self.id_course)


class Curriculum(models.Model):
	cpf = models.OneToOneField(Student,primary_key=True)
	time_desired = models.IntegerField()
	work_shift = models.CharField(max_length=20)
	file_id = models.ForeignKey(File)
	university = models.CharField(max_length=45)
	additional_info = models.CharField(max_length=900)
	semester = models.IntegerField()
	course_id = models.ForeignKey(Course)
	file_id = models.ForeignKey(File)
	class Meta:
		db_table = 'Curriculum'

	def __unicode__(self):
		return '[{}] [{}] {}'.format(self.cpf,self.course_id,self.file_id)


class Requirements(models.Model):
	id_requirements = models.AutoField(primary_key=True)
	work_shift = models.CharField(max_length=20)
	workload = models.IntegerField()
	additional_info = models.CharField(max_length=500)
	minimun_period = models.IntegerField()
	class Meta:
		db_table = 'Requirements'

	def __unicode__(self):
		return '{}'.format(self.id_requirements)


class Vacant_job(models.Model):
	id_vacancy = models.AutoField(primary_key=True)
	role = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	class Meta:
		db_table = 'Vacant_jobs'

	def __unicode__(self):
		return '{}'.format(self.id_vacancy)


class Vacant_job_has_course(models.Model):
	vacant_job_id = models.ForeignKey(Vacant_job)
	course_id = models.ForeignKey(Course)
	class Meta:
		unique_together = ('vacant_job_id','course_id')

	def __unicode__(self):
		return '[{}] [{}]'.format(self.vacant_job_id,self.course_id)


class Vacant_job_has_requirement(models.Model):
    vacant_job_id = models.ForeignKey(Vacant_job)
    requirement_id = models.ForeignKey(Requirements)
    class Meta:
        unique_together = ('vacant_job_id','requirement_id')
    def __unicode__(self):
        return '[{}] [{}]'.format(self.vacant_job_id,self.requirement_id)


class Hiring(models.Model):
	id_hiring = models.AutoField(primary_key=True,)
	contracted_at = models.DateTimeField()
	contract_end = models.DateTimeField()
	active = models.BooleanField()
	id_student = models.ForeignKey(Student)
	id_company = models.ForeignKey(Company)
	id_vacant_job = models.ForeignKey(Vacant_job)
	class Meta:
		db_table = 'Hiring'

	def __unicode__(self):
		return '[{}] [{}] [{}] {}'.format(self.id_student,self.id_company,self.id_vacanct_job,self.id_hiring)


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
		return '{} [{}] [{}]'.format(self.id_review,self.cnpj_company,self.hiring_id)


class Bank_names(models.Model):
	bank_number = models.IntegerField(primary_key=True)
	bank_name = models.CharField(max_length=100)
	class Meta:
		db_table = 'Bank_names'

	def __unicode__(self):
		return self.bank_number


class Bank_accounts(models.Model):
	id_bank_accounts = models.AutoField(primary_key=True)
	account_number = models.CharField(max_length=20)
	agency_number = models.CharField(max_length=10)
	bank_names_bank_number = models.ForeignKey(Bank_names)
	student_cpf = models.ForeignKey(Student)
	class Meta:
		db_table = 'Bank_accounts'

	def __unicode__(self):
return '{} [{}] [{}]'.format(self.id_bank_accounts,self.bank_names_bank_number,self.student_cpf)