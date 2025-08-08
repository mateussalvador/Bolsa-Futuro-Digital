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
def le_e_valida_opcao(min_opcao = 1, max_opcao = 6):
    while True: 
        entrada = input(f"Informe uma opção entre {min_opcao} e {max_opcao}: ")

        if not entrada.isdigit():
            print("ERRO! Digite apenas números.\n")
            continue

        opcao = int(entrada)
        if min_opcao <= opcao <= max_opcao:
            return opcao
        else:
            print(f"ERRO! A opção deve estar entre {min_opcao} e {max_opcao}. Tente novamente.\n")


# Função que verifica se um contato existe
def verifica_contatos_existentes(nome):
    for contato in agenda: 
        if contato["nome"] == nome:
            return True
    return False

# Função que encontra contatos
def encontrar_contato(nome):
    return next((c for c in agenda if c["nome"].lower() == nome.lower()), None) # Se o contato for encontrado, retorna o dicionário. Se não, retorna None (evitando StopIteration)


# Função que adiciona contatos
def adiciona_contatos():
    nome = input("Informe o nome do contato que deseja adicionar: ").lower().strip()
    
    if verifica_contatos_existentes(nome):
        print("ERRO! O contato já está na agenda. Tente novamente.")
        return
    
    endereco = input(f"Informe o endereço de {nome}: ").strip()
    email = input(f"Informe o e-mail de {nome}: ").strip()
    telefone = input(f"Informe o telefone de {nome}: ").strip()

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

# Variável que armazena os dados da agenda de contatos
agenda = []

if __name__ == "__main__":
    while True:
        menu()
        opcao = le_e_valida_opcao()

        match opcao:
            case 1:
                adiciona_contatos()
            case 2:
                edita_contatos()
            case 3:
                busca_contatos()
            case 4:
                print(*lista_contatos(agenda), sep = "\n")
            case 5:
                remove_contato()
            case 6:
                print("Saindo...")
                break              