import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')


cursor = cnx.cursor()
'''
#CONSULTA PARA LOCALIZAR CLIENTE
input_nome = input('Digite o nome do cliente a localizar: ')
valores = (input_nome)
consulta_sql_clientes= "select * from clientes where nome = %s;"
cursor.execute(consulta_sql_clientes,valores)
linhas=cursor.fetchall()
print("Mostrando clientes cadastrados:")
for linha in linhas:
    print("id: ", linha[0])
    print("nome: ", linha[1])
    print("cpf: ", linha[3])
    print("rg: ", linha[4])
    print("cnh: ", linha[5])
    print("sexo: ", linha[6])
    print("endereco: ", linha[7])
    print("email: ", linha[8])
    print("dt_nasc: ", linha[9])
    print("cnpj: ", linha[10])
    print("responsavel: ", linha[11], "\n")


input_nome = input('Digite o nome do cliente a localizar: ')
valores = (input_nome)
consulta_sql_clientes= "select * from clientes where nome like %%s%".format(valores)
cursor.execute(consulta_sql_clientes)
linhas=cursor.fetchall()
print("Mostrando clientes cadastrados:")
for linha in linhas:
    print("id: ", linha[0])
    print("nome: ", linha[1])
    print("cpf: ", linha[3])
    print("rg: ", linha[4])
    print("cnh: ", linha[5])
    print("sexo: ", linha[6])
    print("endereco: ", linha[7])
    print("email: ", linha[8])
    print("dt_nasc: ", linha[9])
    print("cnpj: ", linha[10])
    print("responsavel: ", linha[11], "\n")

'''
consulta_sql_clientes = "select * from clientes where email like '%gmail%'"
cursor.execute(consulta_sql_clientes)
linhas = cursor.fetchall()
print("Mostrando clientes cadastrados:")
for linha in linhas:
    print("id: ", linha[0])
    print("nome: ", linha[1])
    print("cpf: ", linha[2])
    print("rg: ", linha[3])
    print("cnh: ", linha[4])
    print("sexo: ", linha[5])
    print("endereco: ", linha[6])
    print("email: ", linha[7])
    print("dt_nasc: ", linha[8])
    print("cnpj: ", linha[9])
    print("responsavel: ", linha[10], "\n")
