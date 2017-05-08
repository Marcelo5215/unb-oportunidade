from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

#Cogitar a implementação de tp_user

class Student(models.Model):
	cpf = models.CharField(primary_key=True, max_length=11, validators=[RegexValidator(r'^\d{11}$')])
	first_name = models.CharField(max_lenght=45)
	last_name = models.CharField(max_lenght=45)
	email = models.EmailField()
	id_user = models.ForeignKey(User,unique=True)
	phone_number = models.CharField(max_lenght=45)
	regular_student = models.BooleanField()
	class Meta:
		db_table = 'students'

	def __init__(self,cpf,first_name,last_name,email,phone_number,regular_student):
		self.cpf = cpf
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.phone_number = phone_number
		self.regular_student = regular_student

	def __unicode__(self):
		return '[{}] {}'.format(self.id_user,self.cpf)

	def getEmail(self):
		return self.email

	def setEmail(self,email):
		self.email = email

	def getCpf(self):
		return self.cpf

	def getName(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def is_regular(self)
		return self.regular_student

	def getPhone(self):
		return self.phone_number

	def setPhone(self,phone_number):
		self.phone_number = phone_number

class Company(models.Model):
	cnpj = models.AutoField(primary_key=True)
	name = models.CharField(max_lenght=45)
	corporate_name = models.CharField(max_lenght=45)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	address_id = models.ForeignKey(Address)
	id_user = models.ForeignKey(User,unique=True)
	phone_number = models.CharField(max_lenght=45)
	agreement = models.BooleanField()
	class Meta:
		db_table = 'Companies'

	def __init__(self,cnpj,name,corporate_name,phone_number):
		self.cnpj = cnpj
		self.name = name
		self.corporate_name = corporate_name
		self.phone_number = phone_number

	def __unicode__(self):
		return '{} [{}]'.format(self.cnpj,self.address)

	def getCnpj(self):
		return self.cnpj

	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

	def getCorporate_name(self):
		return self.corporate_name

	def setCoporate_name(self,corporate_name):
		self.corporate_name = corporate_name

	def getPhone(self):
		return self.phone_number

	def setPhone(self,phone_number):
		self.phone_number = phone_number




class Curriculum(models.Model):
	cpf = models.ForeignKey(Student,primary_key=True)
	time_desired = models.IntegerField()
	work_shift = models.CharField(max_lenght=20)
	file_id = models.ForeignKey(File)
	university = models.CharField(max_lenght=45)
	additional_info = models.CharField(max_lenght=900)
	semester = models.IntegerField()
	course_id = models.ForeignKey(Course)
	file_id = models.ForeignKey(File)
	class Meta:
		db_table = 'Curriculum'

	def __init__(self,time_desired,work_shift,university,semester,additional_info):
		self.time_desired = time_desired
		self.work_shift = work_shift
		self.university = university
		self.semester = semester
		self.additional_info = additional_info

	def __unicode__(self):
		return '[{}] [{}] {}'.format(self.cpf,self.course_id,self.file_id)

	def getUniversity(self):
		return self.university

	def getTime_desired(self):
		return self.time_desired

	def setTime_desired(self,time_desired):
		self.time_desired = time_desired

	def getSemester(self):
		return self.semester

	def setSemester(self,semester):
		self.semester = semester

	def getInfo(self):
		return self.additional_info

	def setInfo(self,additional_info)
		self.additional_info = additional_info



class Hiring(models.Model):
	id_hiring = models.AutoField(primary_key=True,)
	contracted_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	contract_end = models.DateTimeField(auto_now_add=True, auto_noew=False)
	active = models.BooleanField()
	id_student = models.ForeignKey(Student)
	id_company = models.ForeignKey(Company)
	id_vacancy = models.ForeignKey(Vacant_job)
	class Meta:
		db_table = 'Hiring'

	def __unicode__(self):
		return '[{}] [{}] [{}] {}'.format(self.id_student,self.id_company,self.id_vacancy,self.id_hiring)

	def is_active(self):
		return self.active

	def setActive(self,active):
		self.active = active

class Requirements(models.Model):
	id_requirements = models.AutoField(primary_key=True)
	work_shift = models.CharField(max_lenght=20)
	workload = models.IntegerField()
	additional_info = models.CharField(max_lenght=500)
	minimun_period = models.IntegerField()
	class Meta:
		db_table = 'Requirements'

	def __init__(self,work_shift,workload,minimun_period,additional_info):
		self.work_shift = work_shift
		self.workload = workload
		self.minimun_period = minimun_period
		self.additional_info = additional_info

	def __unicode__(self):
		return '{}'.format(self.id_requirements)

	def getWorkload(self):
		return self.workload

	def setWorkload(self,workload):
		self.workload = workload

	def getWork_shift(self):
		return self.work_shift

	def setWork_shift(self,work_shift):
		self.work_shift = work_shift

	def getMin_period(self):
		return self.minimun_period

	def setMin_period(self,minimun_period):
		self.minimun_period = minimun_period

	def getInfo(self):
		return self.additional_info

	def setInfo(self,additional_info)
		self.additional_info = additional_info


class Address(models.Model):
	id_adress = models.AutoField(primary_key=True)
	city = models.CharField(max_lenght=45)
	neighborhood = models.CharField(max_lenght=45)
	number = models.CharField(max_lenght=4)
	complement = models.CharField(max_lenght=45)
	zip_code = models.CharField(max_lenght=8)
	public_place = models.CharField(max_lenght=45)
	class Meta:
		db_table = 'Address'

	def __init__(self,city,neighborhood,number,complement,zip_code,public_place):
		self.city = city
		self.neighborhood = neighborhood
		self.number = number
		self.complement = complement
		self.zip_code = zip_code
		self.public_place = public_place

	def __unicode__(self):
		return '{}'.format(self.id_adress)

	def getAddress(self):
		address = '%s %s %s %s %s %s' % (self.city, self.neighborhood, self.number,
							 self.public_place, self.complement, self.zip_code)
		return address


class Review(models.Model):
	id_review = models.AutoField(primary_key=True)
	destiny = models.IntegerField()
	stars = models.IntegerField()
	feedback = models.CharField(max_lenght=500)
	cnpj_company = models.ForeignKey(Company)
	hiring_id = models.ForeignKey(Hiring)
	class Meta:
		db_table = 'Reviews'

	def __init__(self,destiny,stars,feedback):
		self.destiny = destiny
		self.stars = stars
		self.feedback = feedback

	def __unicode__(self):
		return '{} [{}] [{}]'.format(self.id_review,self.cnpj_company,self.hiring_id)

	def getDestiny(self):
		return self.destiny

	def getStars(self):
		return self.stars

	def getFeedback(self):
		return self.feedback


#Verificar implementação de FileField
class File(models.Model):
	file_name = models.CharField(max_lenght=500)
	file_path = models.CharField(max_lenght=500)


class Course(models.Model):
	id_course = models.AutoField()
	name = models.CharField(max_lenght=100)
	abbreviation = models.CharField(max_lenght=10)
	class Meta:
		db_table = 'Courses'

	def __init__(self,name,abbreviation):
		self.name = name
		self.abbreviation = abbreviation

	def __unicode__(self):
		return '{}'.format(self.id_course)

class Vacant_job(models.Model):
	id_vacancy = models.AutoField(primary_key=True)
	role = models.CharField(max_lenght=200)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
	class Meta:
		db_table = 'Vacant_jobs'

	def __unicode__(self):
		return '{}'.format(self.id_vacancy)

#Redundante, com o User do Django já é suficiente?
#class Role(models.Model)
	#label = models.CharField(max_lenght=45)

class Bank_accounts(models.Model):
	id_bank_accounts = models.AutoField(primary_key=True)
	account_number = models.CharField(max_lenght=20)
	agency_number = models.CharField(max_lenght=10)
	bank_names_bank_number = models.ForeignKey(Bank_names)
	student_cpf = models.ForeignKey(Student)
	class Meta:
		db_table = 'Bank_accounts'

	def __init__(self,account_number,agency_number):
		self.account_number = account_number
		self.agency_number = agency_number

	def __unicode__(self):
		return '{} [{}] [{}]'.format(self.id_bank_accounts,self.bank_names_bank_number,self.student_cpf)

	def getAccount(self):
		return self.account_number

	def setAccount(self,account_number):
		self.account_number = account_number

	def getAgency(self):
		return self.agency_number

	def setAgency(self,agency_number):
		self.agency_number = agency_number


class Bank_names(models.Model):
	bank_number = models.IntegerField(primary_key=True)
	bank_name = models.CharField(max_lenght=100)
	class Meta:
		db_table = 'Bank_names'

	def __unicode__(self):
		return self.bank_number

