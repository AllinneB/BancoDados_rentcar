import mysql.connector
cnx = mysql.connector.connect(user='root', password='1234', host='localhost',database='rentcar1')


cursor = cnx.cursor()

def consultacliente():
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


def menu():
    print(''' MENU

Escolha um opcao (digite o numero):
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

 ''')

menu()
opcao = int(input('Escolha um opcao (digite o número): '))

if opcao == 1:
    print("\n --- Insira os dados do cliente Pessoa Fisica: ---\n")
consultacliente()

elif opcao == 3:
    print("\n --- Insira os dados do cliente Pessoa Fisica: ---\n")
InserirDadosClientePJ(cnx)

if opcao == 5:
    print("\n --- Lista de clientes cadastrados ---\n")
listar_contato(cnx)

if opcao == 6:
    print("\n --- Insira os dados da cobranca: ---\n")
InserirDadosCobranca(cnx)

if opcao == 9:
    print("\n --- Insira os dados do colaborador: ---\n")
InserirDadosColaborador(cnx)

if opcao == 12:
    print("\n --- Insira os detalhes do tipo da manutencao: ---\n")
InserirDetalhesManutencao(cnx)

if opcao == 15:
print("\n --- Insira os dados do fornecedor: ---\n")
InserirFornecedor(cnx)

if opcao == 18:
    print("\n --- Insira os dados da locacao: ---\n")
InserirLocacao(cnx)

if opcao == 21:
    print("\n --- Insira os dados da manutencao: ---\n")
InserirManutencao(cnx)

if opcao == 24:
    print("\n --- Insira os dados da marca: ---\n")
InserirMarca(cnx)

if opcao == 27:
    print("\n --- Insira os dados do modelo: ---\n")
InserirModelo(cnx)

if opcao == 30:
    print("\n --- Insira os dados do veiculo: ---\n")
InserirVeiculo(cnx)


if opcao == 33:
    exit(cnx)