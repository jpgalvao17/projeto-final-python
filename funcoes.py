import csv

def ler_dados_do_arquivo():
    try:
        with open('pessoas.csv', 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = [pessoa for pessoa in leitor]
            return dados
    except FileNotFoundError:
        return []

def salvar_dados_no_arquivo(dados):
    with open('pessoas.csv', 'w', newline='') as arquivo:
        campos = ['Nome', 'Idade', 'Email', 'Telefone']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)


def print_pessoa(pessoa):
    print(f"\nNome: {pessoa['Nome']}\nIdade: {pessoa['Idade']}\nEmail: {pessoa['Email']}\nTelefone: {pessoa['Telefone']}")


def editar_dados_pessoa(pessoa_editar, novo_nome, novo_idade, novo_email, novo_telefone):
    lista_pessoas = ler_dados_do_arquivo()

    for pessoa in lista_pessoas:
        if pessoa['Nome'] == pessoa_editar['Nome']:
            pessoa['Nome'] = novo_nome
            pessoa['Idade'] = novo_idade
            pessoa['Email'] = novo_email
            pessoa['Telefone'] = novo_telefone

    salvar_dados_no_arquivo(lista_pessoas)


def busca_pessoa(nome_pessoa, pessoas):
    for pessoa in pessoas:
        if (pessoa['Nome'] == nome_pessoa):
            return pessoa
    return None

def salvar_pessoa(nome, idade, email, telefone):
    with open('pessoas.csv', 'a', newline='') as arquivo:
            campos = ['Nome', 'Idade', 'Email', 'Telefone']
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writerow({'Nome': nome, 'Idade': idade, 'Email': email, 'Telefone': telefone})
    print("Pessoa adicionada com sucesso!")