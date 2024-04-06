from funcoes import *

def excluir_pessoa():
    # Faça uma função que exclua uma pessoa do sistema
    # A função deve pedir por input o nome da pessoa, e confirmar a exclusão
    # Use a função buscar_pessoa para buscar a pessoa a ser excluida no sistema
    # Use a função print_pessoa(pessoa) para exibir a pessoa a ser excluida
    # "Você deseja excluir essa pessoa?"
    # Caso ela não seja encontrada, avisar ao usuário "Pessoa nao encontrada"
 return
  

def editar_pessoa():
    # Faça uma função que edite uma pessoa no sistema
    # A função deve pedir o nome da pessoa a ser editada
    # Use a função buscar_pessoa para buscar a pessoa a ser excluida no sistema
    # Use a função print_pessoa(pessoa) para exibir a pessoa a ser editada
    # Use a função editar_dados_pessoa(pessoa_editar, novo_nome, novo_idade, novo_email, novo_telefone) passando
    # os novos dados a serem cadastrados nesta pessoa
    return 

def adicionar_pessoa():
    # Faça uma função que adicione uma pessoa no sistema, pedindo o nome, idade, email e telefone
    # Caso algum dos campos esteja vazio, a função deve printar "Preencha todos os campos" e o usuário deve digitá-lo novamente
    # Use a função  salvar_pessoa(nome, idade, email, telefone): 
    return

def listar_pessoas():
    # Faça uma função que liste todas as pessoas cadastradas no sistema
    # Use a função ler_dados_do_arquivo() para receber uma lista de pessoas
    # Use a função print_pessoa(pessoa) , passando uma pessoa como parâmetro

    return    


def principal():
    #Faça uma função que dê 5 opções para o usuário:

    #1 - Listar pessoas
    #2 - Adicionar pessoa
    #3 - Editar pessoa
    #4 - Excluir pessoa
    #0 - Sair

    # Cada opção deve chamar a função
    #   listar_pessoas()
    #   adicionar_pessoa()
    #   editar_pessoa()
    #   excluir_pessoa()

    # A opção de sair encerra o programa
    
    print("1 - Listar pessoas")
    print("2 - Adicionar pessoa")
    print("3 - Editar pessoa")
    print("4 - Excluir pessoa")
    print("0 - Sair")
 
    usuario = input("qual voce escolhe entre 1 e 4 ou 0 para sair")
    

    if usuario =="1":
        listar_pessoas()
    elif usuario == "2":
        adicionar_pessoa()
    elif usuario == "3":
        editar_pessoa()
    elif usuario == "4":
        excluir_pessoa()
    elif usuario == "0":
        print("voce saiu da lista")
    else: print("opção invalida")
    return

principal()
