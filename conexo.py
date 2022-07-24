import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')

cursor = cnx.cursor()


consulta_sql_clientes= "select * from clientes"
cursor.execute(consulta_sql_clientes)
linhas=cursor.fetchall()
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

consulta_sql_cobranca= "select * from cobranca"
cursor.execute(consulta_sql_cobranca)
linhas=cursor.fetchall()
print("Mostrando cobrancas cadastradas:")
for linha in linhas:
    print("id_cobranca: ", linha[0])
    print("id_locacao: ", linha[1])
    print("valor_locacao: ", linha[2])
    print("id_manutencao: ", linha[3])
    print("vlr_manutencao: ", linha[4], "\n")

    consulta_sql_colaborador = "select * from colaborador"
    cursor.execute(consulta_sql_colaborador)
    linhas = cursor.fetchall()
    print("Mostrando colaboradores cadastrados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("nome: ", linha[1])
        print("cargo: ", linha[2], "\n")

    consulta_sql_manutencao = "select * from detalhes_manutencao"
    cursor.execute(consulta_sql_manutencao)
    linhas = cursor.fetchall()
    print("Mostrando tipos de manutencoes cadastradas:")
    for linha in linhas:
        print("id_manutencao: ", linha[0])
        print("id_tipo_manutencao: ", linha[1])
        print("id_locacao: ", linha[2])
        print("id_fornecedor: ", linha[3], "\n")

    consulta_sql_fornecedor = "select * from fornecedor"
    cursor.execute(consulta_sql_fornecedor)
    linhas = cursor.fetchall()
    print("Mostrando fornecedores cadastrados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("nome: ", linha[1])
        print("cnpj: ", linha[2], "\n")

consulta_sql_locacao= "select * from locacao"
cursor.execute(consulta_sql_locacao)
linhas=cursor.fetchall()
print("Mostrando locacoes cadastradas:")
for linha in linhas:
    print("id: ", linha[0])
    print("data_locacao: ", linha[1])
    print("data_devolucao: ", linha[2])
    print("vlr_diaria: ", linha[3])
    print("vlr_seguro: ", linha[4])
    print("id_veiculo: ", linha[5])
    print("forma_pagamento: ", linha[6])
    print("vlr_locacao: ", linha[7])
    print("id_cliente: ", linha[8])
    print("id_colaborador: ", linha[9], "\n")

consulta_sql_manutencao= "select * from manutencao"
cursor.execute(consulta_sql_manutencao)
linhas=cursor.fetchall()
print("Mostrando manutencoes cadastradas:")
for linha in linhas:
    print("id: ", linha[0])
    print("tipo_manutencao: ", linha[1])
    print("vlr_manutencao: ", linha[2], "\n")

consulta_sql_marca= "select * from marca"
cursor.execute(consulta_sql_marca)
linhas=cursor.fetchall()
print("Mostrando marcas cadastradas:")
for linha in linhas:
    print("id: ", linha[0])
    print("nome: ", linha[1], "\n")

consulta_sql_modelo= "select * from modelo"
cursor.execute(consulta_sql_modelo)
linhas=cursor.fetchall()
print("Mostrando modelos cadastrados:")
for linha in linhas:
    print("id: ", linha[0])
    print("nome: ", linha[1])
    print("id_marca: ", linha[2], "\n")

consulta_sql_veiculo= "select * from veiculo"
cursor.execute(consulta_sql_veiculo)
linhas=cursor.fetchall()
print("Mostrando veiculos cadastrados:")
for linha in linhas:
    print("id_veiculo: ", linha[0])
    print("cor: ", linha[1])
    print("chassi: ", linha[2])
    print("renavan: ", linha[3])
    print("placa: ", linha[4])
    print("id_modelo: ", linha[5])
    print("nivel_combustivel: ", linha[6])
    print("disponivel: ", linha[7])
    print("km: ", linha[8])
    print("classificacao: ", linha[9], "\n")

