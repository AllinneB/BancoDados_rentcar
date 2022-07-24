"""PRINCIPAL"""
import time
import os
import sys
import pymysql
pymysql.install_as_MySQLdb()


def opcaoUsuario():
    print("===================================")
    print("======= MENU ========")
    print("===================================")
    print('''             Escolha um opcao (digite o numero):
                          1 - Inserir Cliente (Pessoa Fisica):
                          2 - Alterar Cliente (Pessoa Fisica):
                          3 - Inserir Cliente (Pessoa Juridica):
                          4 - Alterar Cliente (Pessoa Juridica):
                          5 - Consultar Clientes cadastrados:
                          6 - Inserir Cobranca:
                          7 - Alterar Cobranca:
                          8 - Consultar Cobrancas cadastradas:
                          9 - Inserir Colaborador:
                          10 - Alterar Colaborador:
                          11 - Consultar Colaboradores cadastrados:
                          12 - Inserir tipos de manutencoes:
                          13 - Alterar tipos de manutencoes:
                          14 - Consultar tipos de manuntencoes:
                          15 - Inserir Fornecedor:
                          16 - Alterar Fornecedor:
                          17 - Consultar lista de fornecedores:
                          18 - Inserir Locacao:
                          19 - Alterar Locacao:
                          20 - Consultar Locacoes cadastradas:
                          21 - Inserir Manutencao:
                          22 - Alterar Manutencao:
                          23 - Consultar Manutencoes Cadastradas:
                          24 - Inserir Marca:
                          25 - Alterar Marca:
                          26 - Consultar marcas cadastradas:
                          27 - Inserir Modelo:
                          28 - Alterar Modelo:
                          29 - Consultar modelos cadastrados:
                          30 - Inserir Veiculo:
                          31 - Alterar Veiculo:
                          32 - Consultar veiculos cadastrados:
                          33 - Fechar Menu

                           '''
    )

    opcao = int(input('Escolha um opcao (digite o número): '))

    try:
        opcao = int(opcao)
        if opcao < 1 or opcao > 33:
            os.system("clear");
            print
            "OPCAO INVALIDA: Verifique o valor digitado"
            time.sleep(2)
            opcaoUsuario()
    except:
        os.system("clear");
        print
        "OPCAO INVALIDA: Verifique o valor digitado"
        time.sleep(2)
        opcaoUsuario()

    if opcao == 1:
        conecta = conectaBanco()
        InserirClientePF(conecta)

    elif opcao == 2:
        conecta = conectaBanco()
        funcConsultar(conecta)

    elif opcao == 3:
        conecta = conectaBanco()
        funcAlterar(conecta)

    elif opcao == 4:
        conecta = conectaBanco()
        funcExcluir(conecta)

    elif opcao == 5:
        conecta = conectaBanco()
        funcMostrarTodos(conecta)

    elif opcao == 33:
        sys.exit()


if __name__=='__main__':
    opcaoUsuario()

    # TELA USUARIO

def conectaBanco():
    HOST = "localhost"
    USER = "root"
    PASSWD = "1234"
    BANCO = "rentcar1"

    try:
        conecta = MySQLdb.connect(HOST, USER, PASSWD)
        conecta.select_db(BANCO)

        except MySQLdb.Error:
            e = sys.exc_info()[1]

        print
        "Erro: O banco especificado nao foi encontrado...", e

    menu = raw_input()
    os.system("clear")
    opcaoUsuario()

return conecta
    conecta = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')


def InserirClientePF(conecta):
    print
    "\n\nDigite os dados:\n"
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())
    cpf = str(raw_input("CPF: "))
    cpf = (cpf.upper())
    rg = int(raw_input("RG: "))
    rg = (rg.upper())
    cnh = int(raw_input("CNH: "))
    cnh = (cnh.upper())
    sexo = str(raw_input("Sexo (f/m): "))
    sexo = (sexo.upper())
    endereco = str(raw_input("Endereco: "))
    endereco = (endereco.upper())
    email = str(raw_input("Email: "))
    email = (email.upper())
    telefone = str(raw_input("Email: "))
    telefone = (telefone.upper())
    dt_nasc = str(raw_input("Data de nascimento (Formato AAAA-MM-DD): "))
    dt_nasc = (dt_nasc.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO clientes (nome,cpf,rg,cnh,sexo,endereco,email,telefone,dt_nasc) VALUES ('" + nome + "','" + cpf + "','" + rg + "','" + cnh + ",'" + sexo + ",'" + endereco + ",'" + email + ",'" + telefone + ",'" + dt_nasc + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirClientePJ(conecta):
    print
    "\n\nDigite os dados:\n"
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())
    cpf = str(raw_input("CPF: "))
    cpf = (cpf.upper())
    rg = int(raw_input("RG: "))
    rg = (rg.upper())
    cnh = int(raw_input("CNH: "))
    cnh = (cnh.upper())
    sexo = str(raw_input("Sexo (f/m): "))
    sexo = (sexo.upper())
    endereco = str(raw_input("Endereco: "))
    endereco = (endereco.upper())
    email = str(raw_input("Email: "))
    email = (email.upper())
    telefone = str(raw_input("Email: "))
    telefone = (telefone.upper())
    dt_nasc = str(raw_input("Data de nascimento (Formato AAAA-MM-DD): "))
    dt_nasc = (dt_nasc.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO clientes (nome,cpf,rg,cnh,sexo,endereco,email,telefone,dt_nasc) VALUES ('" + nome + "','" + cpf + "','" + rg + "','" + cnh + ",'" + sexo + ",'" + endereco + ",'" + email + ",'" + telefone + ",'" + dt_nasc + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirColaborador(conecta):
    print
    "\n\nDigite os dados:\n"
    id = int(raw_input("Id: "))
    id = (id.upper())
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())
    cargo = str(raw_input("Cargo: "))
    cargo = (email.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO colaborador (id,nome,cargo) VALUES ('" + id + "','" + nome + "','" + cargo + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirFornecedor(conecta):
    print
    "\n\nDigite os dados:\n"
    id = int(raw_input("Id: "))
    id = (id.upper())
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())
    cnpj = str(raw_input("Cargo: "))
    cnpj = (cnpj.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO fornecedor (id,nome,cnpj) VALUES ('" + id + "','" + nome + "','" + cnpj + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirMarca(conecta):
    print
    "\n\nDigite os dados:\n"
    id = int(raw_input("Id: "))
    id = (id.upper())
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO marca (id,nome) VALUES ('" + id + "','" + nome + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirModelo(conecta):
    print
    "\n\nDigite os dados:\n"
    id = int(raw_input("Id: "))
    id = (id.upper())
    nome = str(raw_input("Nome: "))
    nome = (nome.upper())
    id_marca = int(raw_input("Id marca: "))
    id_marca = (id_marca.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO modelo (id,nome,id_marca) VALUES ('" + id + "','" + nome + "','" + id_marca + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()


def InserirVeiculo(conecta):
    print
    "\n\nDigite os dados:\n"
    id_veiculo = int(raw_input("Id do veiculo: "))
    id_veiculo = (id_veiculo.upper())
    cor = str(raw_input("Cor: "))
    cor = (cor.upper())
    chassi = str(raw_input("Chassi: "))
    chassi = (chassi.upper())
    renavan = str(raw_input("Renavan: "))
    renavan = (renavan.upper())
    placa = str(raw_input("Placa: "))
    placa = (placa.upper())
    id_modelo = int(raw_input("Id do modelo: "))
    id_modelo = (id_modelo.upper())
    nivel_combustivel = str(raw_input("Nivel de combustivel (1, 1/2, 3/4, ): "))
    nivel_combustivel = (nivel_combustivel.upper())
    disponivel = str(raw_input("Disponivel? (S/N): "))
    disponivel = (disponivel.upper())
    km = str(raw_input("Total de kms rodados: "))
    km = (km.upper())
    classificacao = str(raw_input("classificacao: "))
    classificacao = (classificacao.upper())

    cursor = conecta.cursor()

    sql = "INSERT INTO veiculo (id_veiculo,cor,chassi,renavan,placa,id_modelo,nivel_combustivel,disponivel,km,classificacao) VALUES ('" + id_veiculo + "','" + cor + "','" + chassi + "','" + renavan + ",'" + placa + ",'" + id_modelo + ",'" + nivel_combustivel + ",'" + disponivel + ",'" + km + ",'" + classificacao + "')"

    try:
        cursor.execute(sql)
        conecta.commit()


    except MySQLdb.Error:
        e = sys.exc_info()[1]
    print
    "Erro: " + sql
    print
    e


print
"Dados gravados com sucesso."
conecta.close()
menu = raw_input()
os.system("clear")
opcaoUsuario()

print("Rotina para atualização de nome dos clientes no banco de dados")
print("Entre com os dados conforme solicitado:")
print("\nDigite o nome do cliente a alterar:")
nome_atual = input("Nome atual: ")
consulta(nome_atual)
print("\nEntre com o novo nome do cliente:")
novo_nome = input("Nome: ")
altera_sql_clientes = """UPDATE clientes
    SET nome = """ + novo_nome + """
    WHERE nome = """ + nome_atual
atualiza(declaracao)
