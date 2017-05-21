import sqlite3
#Versao desse programa realiza a busca do curso do aluno e imprime na tela o nome e a abreviacao do curso. Atualizar apara pegar lista de oferta das empresas	
conn = sqlite3.connect("../../db.sqlite3")
c = conn.cursor()
c2 = conn.cursor()
c3 = conn.cursor()
surname = 'Almeida'
name = 'Pedro'
student_info = c.execute("SELECT cpf FROM students WHERE first_name=? AND last_name = ?",(name,surname))
for info in student_info:
	#print(info[0])
	curriculum_info = c2.execute("SELECT course_id_id FROM Curriculum WHERE cpf_id = ?",[info[0]])

for course_id in curriculum_info:
	#print(course_id[0])
	course_info = c3.execute("SELECT name,abbreviation FROM Courses where id_course=?",[course_id[0]])

for course_name in course_info:
	print(course_name[0],',',course_name[1])#pega o curso do aluno com sobrenome indicado na variavel surname e imprime na tela a abreviacao do nome do curso e nome completo do curso 

conn.close()

