import sqlite3
conn = sqlite3.connect('teste.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Empresas_Cursos
             (Empresa TEXT,Curso TEXT)''')
c.execute('''CREATE TABLE Alunos
             (Nome TEXT,Curso TEXT) ''')

c.execute("INSERT INTO Alunos VALUES ('Pedro Aurelio' ,'Engenharia da Computacao')")
c.execute("INSERT INTO Alunos VALUES ('Joao' ,'Direito')")
c.execute("INSERT INTO Alunos VALUES ('Maria' ,'Medicina')")
# Insert a row of data
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa1' ,'Engenharia da Computacao')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa2' ,'Engenharia Eletrica')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa3' ,'Direito')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa4' ,'Filosofia')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa5' ,'Medicina')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa7' ,'Direito')")
c.execute("INSERT INTO Empresas_Cursos VALUES ('Empresa1' ,'Ciencia da Computacao')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
