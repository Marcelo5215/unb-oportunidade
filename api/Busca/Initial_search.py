import sqlite3
def tokenize_db_search(string):
	str_tok = str(string).split("'")
	return str_tok[1]
	
conn = sqlite3.connect("teste.db")
c = conn.cursor()#cursor para pesquisa na tablea de alunos
c2 = conn.cursor()#cursor para pesquisa na tabela de empresas
student_name = 'Joao'
courses = c.execute("SELECT Curso FROM Alunos WHERE Nome = ?",[student_name])
for course in courses:
	course_tok  = tokenize_db_search(course)
	companies = c2.execute("SELECT Empresa FROM Empresas_Cursos WHERE Curso = ?",[course_tok])

for company in companies:
	print (tokenize_db_search(company))
conn.close()

