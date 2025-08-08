"""
Faça um programa em python para cadastro de agenda. 

O programa deve utilizar dicionários para cadastrar os contatos, usando como chaves, nome, endereço, e-mail e telefone. Os dicionários devem ser guardados em uma lista.

O menu deve oferecer as seguintes opções: 

1. Adicionar contato - deve verificar se o contato já existe antes de adicionar.

2. Editar contato - deve solicitar o nome de um contato, verificar sua existência e solicitar que o usuário entre com os dados do contato novamente, menos o nome.

3. Buscar contato - deve solicitar o nome de um contato e mostrar os dados.

4. Listar contatos - deve listar os contatos em ordem alfabética.

5. Remover contato - deve remover um contato existente.

6. Sair.

Usar funções.
"""

import os

# Variável global que armazenará a lista de contatos
agenda = []

# Função que printa o menu
def menu():
    print("---------- MENU ----------\n")
    print("1. Adicionar contato - deve verificar se o contato já existe antes de adicionar.")
    print("2. Editar contato - deve solicitar o nome de um contato, verificar sua existência e solicitar que o usuário entre com os dados do contato novamente, menos o nome.")
    print("3. Buscar contato - deve solicitar o nome de um contato e mostrar os dados.")
    print("4. Listar contatos - deve listar os contatos em ordem alfabética.")
    print("5. Remover contato - deve remover um contato existente.")
    print("6. Sair.\n")


# Função que valida a opção escolhida pelo usuário
def le_e_valida_opcao():
    while True: 
        try:
            opcao = int(input("Informe o número da operação que deseja realizar: "))

            if opcao < 1 or opcao > 6:
                raise ValueError
            
            return opcao
            
        except ValueError:
            print("ERRO! Por favor, insira uma opção de numérica entre 1 e 6. Tente novamente.")


# Função que verifica se um contato existe
def verifica_contatos_existentes(nome):
    for contato in agenda: 
        if contato["nome"] == nome:
            return True
        
    return False


# Função que adiciona contatos
def adiciona_contatos():
    nome = input("Informe o nome do contato que deseja adicionar: ")
    
    if verifica_contatos_existentes(nome):
        print("ERRO! O contato já está na agenda. Tente novamente.")
        return
    
    endereco = input(f"Informe o endereço de {nome}: ")
    email = input(f"Informe o e-mail de {nome}: ")
    telefone = input(f"Informe o telefone de {nome}: ")

    contato = {
        "nome": nome,
        "endereco": endereco,
        "email": email,
        "telefone": telefone,
    }

    agenda.append(contato)

    return "Contato adicionado com sucesso."


# Função que edita contatos
def edita_contatos():
    if len(agenda) == 0:
        print("Você não pode editar uma agenda vazia.")
        return

    nome = input("Informe o nome do contato que você deseja editar: ")

    if not verifica_contatos_existentes(nome):
        print("ERRO! O contato não existe. Por favor, tente novamente.")
        return
    
    for contato in agenda:
        if contato["nome"] == nome:
            print(f"Insira os novos dados de {nome}:")
            contato["endereco"] = input("Endereço: ")
            contato["email"] = input("E-mail: ")
            contato["telefone"] = input("Telefone: ")

            print("Contato editado com sucesso.")
    return


# Função que busca contatos
def busca_contatos():
    if len(agenda) == 0:
        print("Você ainda não possui contatos.")
        return

    nome = input("Informe o nome do contato que você deseja buscar: ")

    if not verifica_contatos_existentes(nome):
        print("Este contato não existe. Tente novamente.")
        return
    
    for contato in agenda:
        if contato["nome"] == nome:
            for chave, valor in contato.items():
                print(f"{chave}: {valor}")

    return
    
# Função que lista contatos
def lista_contatos(agenda):
    if len(agenda) == 0:
        return "Você ainda não possui contatos."
    return sorted(agenda, key = lambda agenda: agenda["nome"])

# Função que remove contatos
def remove_contato():
    if len(agenda) == 0:
        print("Você ainda não possui contatos.")
        return

    nome = input("Informe o nome do contato que você deseja remover: ")

    if not verifica_contatos_existentes(nome):
        print("Este contato não existe. Tente novamente.")
        return
    
    for contato in agenda:
        if contato["nome"] == nome:
            agenda.remove(contato)
            print("Contato removido com sucesso.")
    return
    

# Execução
if __name__ == "__main__":
    while True:
        os.system("cls") 
        menu()
        opcao = le_e_valida_opcao()

        match opcao:
            case 1:
                adiciona_contatos()
                os.system("pause")
            case 2:
                edita_contatos()
                os.system("pause")
            case 3:
                busca_contatos()
                os.system("pause")
            case 4:
                print(*lista_contatos(agenda), sep = "\n")
                os.system("pause")
            case 5:
                remove_contato()
                os.system("pause")
            case 6:
                print("Saindo...")
                break              