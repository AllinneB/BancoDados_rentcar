import mysql.connector
from mysql.connector import Error

# Script para atualização de registros em um banco de dados MySQL

def conectar():
    try:
        global cnx
        cnx = mysql.connector.connect(user='root', password='1234', host='localhost', database='rentcar1')
    except Error as erro:
        print("Erro de Conexão")


def atualiza(altera_sql_clientes):
    try:
        conectar()
        altera_nome = altera_sql_clientes
        cursor = cnx.cursor()
        cursor.execute(altera_nome)
        cnx.commit()
        print("Nome alterado com sucesso!")
        cursor.close()
    except Error as erro:
        print("Falha ao inserir dados no MySQL: {}".format(erro))
    finally:
        if (cnx.is_connected()):
            cursor.close()
            cnx.close()


def consulta(nome_atual):
    try:
        conectar()
        consulta_sql = 'select * from clientes WHERE nome =' + nome_atual
        cursor = cnx.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        for linha in linhas:
            print("id: ", linha[0])
            print("nome: ", linha[1])
            print("endereco: ", linha[2])
    except Error as erro:
        print("Falha ao consultar tabela: {}".format(erro))
    finally:
        if (cnx.is_connected()):
            cursor.close()
            cnx.close()


# Programa principal
if __name__ == '__main__':

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
    atualiza(altera_sql_clientes)

    verifica = input("\nDeseja consultar a atualização? s = Sim, n = Não\n")
    if (verifica == 's'):
        consulta(nome_atual)
    else:
        print("\nAté mais!")
