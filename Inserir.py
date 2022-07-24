import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')

cursor = cnx.cursor()

'''
#INSERIR CLIENTE PESSOA FISICA
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
valores = (input_id,input_nome,input_cpf,input_rg,input_cnh,input_sexo,input_endereco,input_email,input_telefone,input_dt_nasc)
cursor.execute(comando_sql,valores)
cnx.commit()

#INSERIR CLIENTE PESSOA JURIDICA
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


#INSERINDO DADOS DE COBRANCA
input_id_cobranca = input('Digite o id da cobranca a ser cadastrada: ')
input_id_locacao = input('Digite o id da locacao a ser cadastrada: ')
input_valor_locacao = input('Digite o valor da locacao a ser cadastrada: ')
input_id_manutencao = input('Digite o id da manutencao a ser cadastrada: ')
input_vlr_manutencao = input('Digite o valor da manutencao a ser cadastrada: ')
comando_sql = "INSERT INTO cobranca(id_cobranca,id_locacao,valor_locacao,id_manutencao,vlr_manutencao) VALUES(%s,%s,%s,%s,%s)"
valores = (input_id_cobranca,input_id_locacao,input_valor_locacao,input_id_manutencao,input_vlr_manutencao)
cursor.execute(comando_sql,valores)
cnx.commit()

#INSERINDO DADOS DE COLABORADOR
input_id = input('Digite o id do colaborador a ser cadastrado: ')
input_nome = input('Digite o nome do colaborador a ser cadastrado: ')
input_cargo = input('Digite o cargo do colaborador a ser cadastrado: ')
comando_sql = "INSERT INTO colaborador(id,nome,cargo) VALUES(%s,%s,%s)"
valores = (input_id,input_nome,input_cargo)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO DETALHES MANUTENCAO
input_id_manutencao = input('Digite o id da manutenção a ser cadastrada: ')
input_id_tipo_manutencao = input('Digite o id do tipo de manutenção a ser cadastrada: ')
input_vlr_manutencao = input('Digite o valor da manutenção a ser cadastrada: ')
input_id_locacao = input('Digite o id da locacao ser cadastrada: ')
input_id_fornecedor = input('Digite o id do fornecedor a ser cadastrado: ')
comando_sql = "INSERT INTO detalhes_manutencao(id_manutencao,id_tipo_manutencao,vlr_manutencao,id_locacao,id_fornecedor) VALUES(%s,%s,%s,%s,%s)"
valores = (input_id_manutencao,input_id_tipo_manutencao,input_vlr_manutencao,input_id_locacao,input_id_fornecedor)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO FORNECEDORES
input_id = input('Digite o id do fornecedor a ser cadastrado: ')
input_nome = input('Digite o nome do fornecedor a ser cadastrado: ')
input_cnpj = input('Digite o cnpj do fornecedor a ser cadastrado (formato xx.xxx.xxx/xxxx-xx): ')
comando_sql = "INSERT INTO fornecedor(id,nome,cnpj) VALUES(%s,%s,%s)"
valores = (input_id,input_nome,input_cnpj)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO DADOS DE LOCACAO
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
valores = (input_id,input_data_locacao,input_data_devolucao,input_vlr_diaria,input_vlr_seguro,input_id_veiculo,input_forma_pagamento,input_valor_locacao,input_id_cliente,input_id_colaborador)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO DADOS DE MANUTENCAO
input_id = input('Digite o id do tipo de manutencao: ')
input_tipo_manutencao = input('Digite o nome da manutencao: ')
input_vlr_manutencao = input('Digite o valor padrao do serviço de manutencao: ')
comando_sql = "INSERT INTO manutencao(id,tipo_manutencao,vlr_manutencao) VALUES(%s,%s,%s)"
valores = (input_id,input_tipo_manutencao,input_vlr_manutencao)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO DADOS DE MARCA
input_id = input('Digite o id da marca a ser cadastrada: ')
input_nome = input('Digite o nome da marca a ser cadastrada: ')
comando_sql = "INSERT INTO marca(id,nome) VALUES(%s,%s)"
valores = (input_id,input_nome)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()

#INSERINDO DADOS DE MODELO
input_id = input('Digite o id do modelo do veiculo: ')
input_nome = input('Digite o nome do modelo do veiculo: ')
input_id_marca = input('Digite o id da marca do veiculo: ')
comando_sql = "INSERT INTO modelo(id,nome,id_marca) VALUES(%s,%s,%s)"
valores = (input_id,input_nome,input_id_marca)
cursor.execute(comando_sql,valores)
'''
#INSERINDO DADOS DE VEICULO
input_id_veiculo = input('Digite o do veiculo a cadastrar: ')
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
valores = (input_id_veiculo,input_cor,input_chassi,input_renavan,input_placa,input_id_modelo,input_nivel_combustivel,input_disponivel,input_km,input_classificacao)
cursor.execute(comando_sql,valores)

cnx.commit()
cursor.close()