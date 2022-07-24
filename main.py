#CONSULTANDO DADOS NO PYTHON - Tabela modelo

import mysql

cnx = pymysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')

cursor = cnx.cursor()
consulta_sql= "select * from modelo"
cursos=cnx.cursor()
cursor.execute(consulta_sql)
linhas=cursor.fetchall()
print("Mostrando modelos cadastrados")
for linha in linhas:
	print("id: ", linha[0])
	print("nome: ", linha[1])
	print("id_marca: ", linha[2], "\n")