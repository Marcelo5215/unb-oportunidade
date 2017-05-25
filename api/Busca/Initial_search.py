import sqlite3
#Versao desse programa realiza a busca da lista de oferta das empresas cujo curso pre-requisito eh compativel com o curso do aluno. Atualizar para a primeira busca ja ser com o user ID	
conn = sqlite3.connect("../../db.sqlite3")
c = conn.cursor()
c2 = conn.cursor()
c3 = conn.cursor()
c4 = conn.cursor()
c5 = conn.cursor()
surname = 'Almeida'
name = 'Pedro'
student_info = c.execute("SELECT cpf FROM students WHERE first_name=? AND last_name = ?",(name,surname))
for info in student_info:	
	curriculum_info = c2.execute("SELECT course_id_id FROM Curriculum WHERE cpf_id = ?",[info[0]])

for course_id in curriculum_info:
	vacant_job_info = c3.execute("SELECT vacant_job_id_id FROM Vacant_job_has_course where course_id_id=?",[course_id[0]])

companies_cnpj=[]

for vacant_job in vacant_job_info:
	sql_companies_id = c4.execute("SELECT id_company_id FROM Hiring where id_vacancy_id=?",[vacant_job[0]])
	for sql_company_id in sql_companies_id:
		companies_cnpj.append(sql_company_id[0])
	
companies_name = []
for company_id in companies_cnpj:
	sql_companies_name = c5.execute("SELECT name FROM Companies where cnpj=?",[company_id])
	for sql_company_name in sql_companies_name:	
		companies_name.append(sql_company_name[0])

for company in companies_name:
	print(company)#pega o nome das empresas cujo curso pre-requisito eh compativel com o curso do aluno 

conn.close()

