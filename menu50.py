import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')

cursor = cnx.cursor()

def InserirClientePF():
    input_id = input('Digite o id do cliente a ser cadastrado: ')
    input_nome = input('Digite o nome do cliente a ser cadastrado: ')
    input_cpf = input('Digite o cpf do cliente a ser cadastrado: ')
    input_rg = input('Digite o rg do cliente a ser cadastrado: ')
    input_cnh = input('Digite a cnh do cliente a ser cadastrado: ')
    input_sexo = input('Digite o sexo do cliente a ser cadastrado (F/M): ')
    input_endereco = input('Digite o endereco do cliente a ser cadastrado: ')
    input_email = input('Digite o email do cliente a ser cadastrado: ')
    input_telefone = input('Digite o telefone do cliente a ser cadastrado: ')
    input_dt_nasc = input('Digite a data de nascimento do cliente a ser cadastrado (AAAA-MM-DD): ')

    comando_sql = "INSERT INTO clientes(id,nome,cpf,rg,cnh,sexo,endereco,email,telefone,dt_nasc) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (
    input_id, input_nome, input_cpf, input_rg, input_cnh, input_sexo, input_endereco, input_email, input_telefone,
    input_dt_nasc)
    cursor.execute(comando_sql, valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteracliente():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o nome do cliente a alterar:")
    nome_atual = input("Nome atual: ")
    novo_nome = input("Novo nome: ")
    novo_nome = (novo_nome.upper())

    sql = "UPDATE clientes SET nome='" + novo_nome + "' WHERE nome='" + nome_atual + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultacliente():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o nome do cliente a consultar:")
    nome_atual = input("Nome ou parte do nome: ")

    consulta_sql_clientes = "select * from clientes where nome like'%" + nome_atual + "%'"
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
        print("telefone: ", linha[8])
        print("dt_nasc: ", linha[9])
        print("responsavel: ", linha[10], "\n")

        opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

        if (opcaomenu == 1):
            menu()

        else:
            print("Conexão encerrada")

        cursor.close()
        cnx.close()

def InserirClientePJ():
    input_id = input('Digite o id do cliente a ser cadastrado: ')
    input_nome = input('Digite o nome do cliente a ser cadastrado: ')
    input_cnpj = input('Digite o cnpj do cliente a ser cadastrado: ')
    input_endereco = input('Digite o endereco do cliente a ser cadastrado: ')
    input_email = input('Digite o email do cliente a ser cadastrado: ')
    input_telefone = input('Digite o telefone do cliente a ser cadastrado: ')
    input_responsavel = input('Digite o nome do responsavel pela empresa a ser cadastrada: ')
    comando_sql = "INSERT INTO clientes(id,nome,cnpj,endereco,email,telefone,responsavel) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    valores = (input_id,input_nome,input_cnpj,input_endereco,input_email,input_telefone,input_responsavel)
    cursor.execute(comando_sql,valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()


def Inserir_cobranca():
    input_id_cobranca = input('Digite o id da cobranca a ser cadastrada: ')
    input_id_locacao = input('Digite o id da locacao a ser cadastrada: ')
    input_valor_locacao = input('Digite o valor da locacao a ser cadastrada: ')
    input_id_manutencao = input('Digite o id da manutencao a ser cadastrada: ')
    input_vlr_manutencao = input('Digite o valor da manutencao a ser cadastrada: ')
    comando_sql = "INSERT INTO cobranca(id_cobranca,id_locacao,valor_locacao,id_manutencao,vlr_manutencao) VALUES(%s,%s,%s,%s,%s)"
    valores = (input_id_cobranca, input_id_locacao, input_valor_locacao, input_id_manutencao, input_vlr_manutencao)
    cursor.execute(comando_sql, valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()


def alteracobranca():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id da cobranca a alterar o valor da locacao:")
    id_cobranca = input("Id cobranca: ")
    novo_valor = input("Novo valor da locacao: ")
    novo_valor = (novo_valor.upper())

    sql = "UPDATE cobranca SET valor_locacao='" + novo_valor + "' WHERE id_cobranca='" + id_cobranca + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultacobranca():
    consulta_sql_cobranca = "select * from cobranca"
    cursor.execute(consulta_sql_cobranca)
    linhas = cursor.fetchall()
    print("Mostrando cobrancas cadastradas:")
    for linha in linhas:
        print("id_cobranca: ", linha[0])
        print("id_locacao: ", linha[1])
        print("valor_locacao: ", linha[2])
        print("id_manutencao: ", linha[3])
        print("valor_manutencao: ", linha[4], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

#INSERINDO DADOS DE COLABORADOR
def Inserir_colaborador():
    input_id = input('Digite o id do colaborador a ser cadastrado: ')
    input_nome = input('Digite o nome do colaborador a ser cadastrado: ')
    input_cargo = input('Digite o cargo do colaborador a ser cadastrado: ')
    comando_sql = "INSERT INTO colaborador(id,nome,cargo) VALUES(%s,%s,%s)"
    valores = (input_id,input_nome,input_cargo)
    cursor.execute(comando_sql,valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteracolaborador():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id do colaborador a alterar o cargo:")
    id_atual = input("Id: ")
    novo_cargo = input("Novo cargo do colaborador: ")
    novo_cargo = (novo_cargo.upper())

    sql = "UPDATE colaborador SET cargo ='" + novo_cargo + "' WHERE id='" + id_atual + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultacolaborador():
    consulta_sql_colaborador = "select * from colaborador"
    cursor.execute(consulta_sql_colaborador)
    linhas = cursor.fetchall()
    print("Mostrando colaboradores cadastrados:")
    for linha in linhas:
        print("Id: ", linha[0])
        print("Nome: ", linha[1])
        print("Cargo: ", linha[2], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()


def Inserirdetalhesmanutencoes():
    # INSERINDO DETALHES MANUTENCAO
    input_id_manutencao = input('Digite o id da manutenção a ser cadastrada: ')
    input_id_tipo_manutencao = input('Digite o id do tipo de manutenção a ser cadastrada: ')
    input_vlr_manutencao = input('Digite o valor da manutenção a ser cadastrada: ')
    input_id_locacao = input('Digite o id da locacao ser cadastrada: ')
    input_id_fornecedor = input('Digite o id do fornecedor a ser cadastrado: ')
    comando_sql = "INSERT INTO detalhes_manutencao(id_manutencao,id_tipo_manutencao,vlr_manutencao,id_locacao,id_fornecedor) VALUES(%s,%s,%s,%s,%s)"
    valores = (
    input_id_manutencao, input_id_tipo_manutencao, input_vlr_manutencao, input_id_locacao, input_id_fornecedor)
    cursor.execute(comando_sql, valores)

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteradetalhesmanutencoes():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite a id da manutencao efetuada para a qual será alterado o valor:")
    id_atual = input("Id: ")
    novo_valor = input("Novo valor da manutencao realizada: ")
    novo_valor = (novo_valor.upper())

    sql = "UPDATE detalhes_manutencao SET vlr_manutencao ='" + novo_valor + "' WHERE id_manutencao='" + id_atual + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultadetalhesmanutencoes():
    consulta_sql_det = "select * from detalhes_manutencao"
    cursor.execute(consulta_sql_det)
    linhas = cursor.fetchall()
    print("Mostrando manutencoes cadastradas:")
    for linha in linhas:
        print("id_manutencao: ", linha[0])
        print("id_tipo_manutencao: ", linha[1])
        print("vlr_manutencao: ", linha[2])
        print("id_locacao: ", linha[3])
        print("id_fornecedor: ", linha[4], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

#INSERINDO FORNECEDORES
def Inserirfornecedores():
    input_id = input('Digite o id do fornecedor a ser cadastrado: ')
    input_nome = input('Digite o nome do fornecedor a ser cadastrado: ')
    input_cnpj = input('Digite o cnpj do fornecedor a ser cadastrado (formato xx.xxx.xxx/xxxx-xx): ')
    comando_sql = "INSERT INTO fornecedor(id,nome,cnpj) VALUES(%s,%s,%s)"
    valores = (input_id,input_nome,input_cnpj)
    cursor.execute(comando_sql,valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alterafornecedor():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite a id do fornecedor a alterar o nome:")
    id_atual = input("Id atual: ")
    novo_nome = input("Novo nome: ")
    novo_nome = (novo_nome.upper())

    sql = "UPDATE fornecedor SET nome='" + novo_nome + "' WHERE id='" + id_atual + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultafornecedor():
    consulta_sql_fornecedor = "select * from fornecedor"
    cursor.execute(consulta_sql_fornecedor)
    linhas = cursor.fetchall()
    print("Mostrando fornecedores cadastrados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("nome: ", linha[1])
        print("cnpj: ", linha[2], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def Inserirlocacao():
    input_id = input('Digite o id da locacao a ser cadastrada: ')
    input_data_locacao = input('Digite a data da locacao a ser cadastrada (AAAA-MM-DD): ')
    input_data_devolucao = input('Digite a data de devolucao do veiculo (AAAA-MM-DD): ')
    input_vlr_diaria = input('Digite o valor da diaria da locacao: ')
    input_vlr_seguro = input('Digite o valor do seguro da locacao: ')
    input_id_veiculo = input('Digite o id do veiculo locado: ')
    input_forma_pagamento = input('Digite a forma de pagamento da locacao: ')
    input_valor_locacao = input('Digite o valor total da locacao: ')
    input_id_cliente = input('Digite o id do cliente que efetuou a locacao ')
    input_id_colaborador = input('Digite o id do colaborador que efetuou a locacao ')
    comando_sql = "INSERT INTO locacao(id,data_locacao,data_devolucao,vlr_diaria,vlr_seguro,id_veiculo,forma_pagamento,valor_locacao,id_cliente,id_colaborador) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (input_id, input_data_locacao, input_data_devolucao, input_vlr_diaria, input_vlr_seguro, input_id_veiculo,
               input_forma_pagamento, input_valor_locacao, input_id_cliente, input_id_colaborador)
    cursor.execute(comando_sql, valores)

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteralocacao():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id da locacao a alterar o valor da diaria:")
    id_locacao = input("Id locacao: ")
    novo_valor = input("Novo valor da locacao: ")
    novo_valor = (novo_valor.upper())

    sql = "UPDATE locacao SET vlr_diaria='" + novo_valor + "' WHERE id='" + id_locacao + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultalocacao():
    consulta_sql_locacao = "select * from locacao"
    cursor.execute(consulta_sql_locacao)
    linhas = cursor.fetchall()
    print("Mostrando locacoes cadastradas:")
    for linha in linhas:
        print("id: ", linha[0])
        print("data da locacao: ", linha[1])
        print("data de devolucao: ", linha[2])
        print("valor da diaria: ", linha[3])
        print("valor do seguro: ", linha[4])
        print("id do veiculo: ", linha[5])
        print("forma de pagamento: ", linha[6])
        print("valor da locacao: ", linha[7])
        print("id do cliente: ", linha[8])
        print("id do colaborador que efetuou a locacao ", linha[9], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

#INSERINDO DADOS DE MANUTENCAO
def Inserirtipomanutencao():
    input_id = input('Digite o id do tipo de manutencao: ')
    input_tipo_manutencao = input('Digite o nome da manutencao: ')
    input_vlr_manutencao = input('Digite o valor padrao do serviço de manutencao: ')
    comando_sql = "INSERT INTO manutencao(id,tipo_manutencao,vlr_manutencao) VALUES(%s,%s,%s)"
    valores = (input_id,input_tipo_manutencao,input_vlr_manutencao)
    cursor.execute(comando_sql,valores)

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteratipomanutencao():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id do tipo de manutencao a alterar o nome:")
    id_manutencao = input("Id manutencao: ")
    novo_titulo = input("Novo titulo/nome da manutencao: ")
    novo_titulo = (novo_titulo.upper())

    sql = "UPDATE manutencao SET tipo_manutencao='" + novo_titulo + "' WHERE id='" + id_manutencao + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultatipomanutencao():
    consulta_sql_tipomanut = "select * from manutencao"
    cursor.execute(consulta_sql_tipomanut)
    linhas = cursor.fetchall()
    print("Mostrando tipos de manutencoes cadastradas:")
    for linha in linhas:
        print("id: ", linha[0])
        print("nome: ", linha[1])
        print("valor médio ", linha[2], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

 # INSERINDO DADOS DE MARCA
def inserirmarca():
    input_id = input('Digite o id da marca a ser cadastrada: ')
    input_nome = input('Digite o nome da marca a ser cadastrada: ')
    comando_sql = "INSERT INTO marca(id,nome) VALUES(%s,%s)"
    valores = (input_id, input_nome)
    cursor.execute(comando_sql, valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteramarca():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id da marca a alterar o nome:")
    id_marca = input("Id da marca: ")
    novo_titulo = input("Novo titulo/nome da marca: ")
    novo_titulo = (novo_titulo.upper())

    sql = "UPDATE marca SET nome='" + novo_titulo + "' WHERE id='" + id_marca + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()


def consultamarca():
    consulta_sql_marca = "select * from marca"
    cursor.execute(consulta_sql_marca)
    linhas = cursor.fetchall()
    print("Mostrando marcas cadastradas:")
    for linha in linhas:
        print("id: ", linha[0])
        print("Nome da marca: ", linha[1], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def inserirmodelo():
    # INSERINDO DADOS DE MODELO
    input_id = input('Digite o id do modelo do veiculo: ')
    input_nome = input('Digite o nome do modelo do veiculo: ')
    input_id_marca = input('Digite o id da marca do veiculo: ')
    comando_sql = "INSERT INTO modelo(id,nome,id_marca) VALUES(%s,%s,%s)"
    valores = (input_id, input_nome, input_id_marca)
    cursor.execute(comando_sql, valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteramodelo():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id do modelo a alterar o nome:")
    id_modelo = input("Id modelo: ")
    novo_titulo = input("Novo titulo/nome do modelo: ")
    novo_titulo = (novo_titulo.upper())

    sql = "UPDATE modelo SET nome='" + novo_titulo + "' WHERE id='" + id_modelo + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultamodelo():
    consulta_sql_modelo = "select modelo.id, modelo.nome, marca.nome from modelo inner join marca on modelo.id_marca = marca.id"
    #consulta_sql_modelo = "select * from modelo inner join marca on modelo.id_marca = marca.id"
    cursor.execute(consulta_sql_modelo)
    linhas = cursor.fetchall()
    print("Mostrando modelos cadastrados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("Nome do modelo: ", linha[1])
        print("Nome da marca associada ao modelo: ", linha[2], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

#INSERINDO DADOS DE VEICULO
def inserirveiculo():
    input_id_veiculo = input('Digite o id do veiculo a cadastrar: ')
    input_cor = input('Digite a cor do veiculo: ')
    input_chassi = input('Digite o chassi do veiculo: ')
    input_renavan = input('Digite o renavan do veiculo: ')
    input_placa = input('Digite a placa do veiculo: ')
    input_id_modelo = input('Digite id do modelo do veiculo: ')
    input_nivel_combustivel = input('Digite o nivel do combustivel (1/4,1/2,3/4, ou 1): ')
    input_disponivel = input('O veiculo está disponível? (Informe S ou N): ')
    input_km = input('Digite o total de kms rodados: ')
    input_classificacao = input('Digite a classificacao do veiculo: ')
    comando_sql = "INSERT INTO veiculo(id_veiculo,cor,chassi,renavan,placa,id_modelo,nivel_combustivel,disponivel,km,classificacao) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valores = (
    input_id_veiculo, input_cor, input_chassi, input_renavan, input_placa, input_id_modelo, input_nivel_combustivel,
    input_disponivel, input_km, input_classificacao)
    cursor.execute(comando_sql, valores)
    cnx.commit()

    print("\nDados gravados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def alteraveiculo():
    print("Entre com os dados conforme solicitado:")
    print("\nDigite o id do veiculo a alterar a cor:")
    id_veiculo = input("Id veiculo: ")
    nova_cor = input("Nova cor do veiculo: ")
    nova_cor = (nova_cor.upper())

    sql = "UPDATE veiculo SET cor='" + nova_cor + "' WHERE id_veiculo='" +  id_veiculo + "'"
    cursor.execute(sql)
    cnx.commit()

    print("\nDados alterados com sucesso.\n")
    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()

def consultaveiculo():
    consulta_sql_veiculo = "select * from veiculo"
    cursor.execute(consulta_sql_veiculo)
    linhas = cursor.fetchall()
    print("Mostrando veiculos cadastrados:")
    for linha in linhas:
        print("id: ", linha[0])
        print("Cor: ", linha[1])
        print("Chassi: ", linha[2])
        print("Renavan: ", linha[3])
        print("Placa: ", linha[4])
        print("Id do modelo: ", linha[5])
        print("Nivel de combustivel: ", linha[6])
        print("Disponivel? (S/N): ", linha[7])
        print("Quilometragem: ", linha[8])
        print("Classificacao: ", linha[9], "\n")

    opcaomenu = int(input('\n Deseja retornar ao menu principal? Digite 1 para sim e 2 para não: \n '))

    if (opcaomenu == 1):
        menu()

    else:
        print("Conexão encerrada")

    cursor.close()
    cnx.close()


def menu():
    print(''' \nMENU\n''')
    opcao = int(input('1 - Inserir Cliente (Pessoa Fisica): \n2 - Alterar Nome de Cliente: \n3 - Inserir Cliente (Pessoa Juridica):\n4 - Consultar Clientes cadastrados:\n5 - Inserir Cobranca:\n6 - Alterar Cobranca:\n7 - Consultar Cobrancas cadastradas:\n8 - Inserir Colaborador: \n9 - Alterar Colaborador:\n10 - Consultar Colaboradores cadastrados:\n11 - Inserir tipos de manutencoes:\n12 - Alterar tipos de manutencoes:\n13 - Consultar tipos de manuntencoes: \n14 - Inserir Fornecedor: \n15 - Alterar Fornecedor: \n16 - Consultar lista de fornecedores:\n17 - Inserir Locacao:\n18 - Alterar Locacao:\n19 - Consultar Locacoes cadastradas:\n20 - Inserir Manutencao:\n21 - Alterar Manutencao:\n22 - Consultar Manutencoes Cadastradas:\n23 - Inserir Marca:\n24 - Alterar Marca:\n25 - Consultar marcas cadastradas:\n26 - Inserir Modelo:\n27 - Alterar Modelo:\n28 - Consultar modelos cadastrados:\n29 - Inserir Veiculo:\n30 - Alterar Veiculo:\n31 - Consultar veiculos cadastrados:\n32 - Fechar Menu\n\nEscolha uma opcao (digite o número): '))

    if opcao == 1:
        InserirClientePF()
    elif opcao == 2:
        alteracliente()
    elif opcao == 3:
        InserirClientePJ()
    elif opcao == 4:
        consultacliente()
    elif opcao == 5:
        Inserir_cobranca()
    elif opcao == 6:
        alteracobranca()
    elif opcao == 7:
        consultacobranca()
    elif opcao == 8:
        Inserir_colaborador()
    elif opcao == 9:
        alteracolaborador()
    elif opcao == 10:
        consultacolaborador()
    elif opcao == 11:
        Inserirdetalhesmanutencoes()
    elif opcao == 12:
        alteradetalhesmanutencoes()
    elif opcao == 13:
        consultadetalhesmanutencoes()
    elif opcao == 14:
        Inserirfornecedores()
    elif opcao == 15:
        alterafornecedor()
    elif opcao == 16:
        consultafornecedor()
    elif opcao == 17:
        Inserirlocacao()
    elif opcao == 18:
        alteralocacao()
    elif opcao == 19:
        consultalocacao()
    elif opcao == 20:
        Inserirtipomanutencao()
    elif opcao == 21:
        alteratipomanutencao()
    elif opcao == 22:
        consultatipomanutencao()
    elif opcao == 23:
        inserirmarca()
    elif opcao == 24:
        alteramarca()
    elif opcao == 25:
        consultamarca()
    elif opcao == 26:
        inserirmodelo()
    elif opcao == 27:
        alteramodelo()
    elif opcao == 28:
        consultamodelo()
    elif opcao == 29:
        inserirveiculo()
    elif opcao == 30:
        alteraveiculo()
    elif opcao == 31:
        consultaveiculo()
    elif opcao == 32:
        exit(cnx)
    elif opcao <1 or opcao>32:
        print("OPCAO INVALIDA: Verifique o valor digitado")

menu()