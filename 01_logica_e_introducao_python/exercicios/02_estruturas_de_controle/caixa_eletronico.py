# Crie um programa que simule o funcionamento de um caixa eletrônico. O usuário inicia com um saldo fictício e pode realizar as seguintes operações através de um menu iterativo:
# 1. Consultar saldo
# 2. Depositar dinheiro
# 3. Sacar dinheiro
# 4. Sair
#  O programa deve repetir o menu até o usuário escolher a opção 4 (sair).

saldo = 200.00

while True:
    print("\n\n--- MENU ---")
    print("1. Consultar saldo")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. Sair")

    try:
        opcao = int(input("Informe o número da operação que deseja realizar: "))
    except ValueError:
        print("ERRO! A opção deve ser um número de 1 a 4. Tente novamente.")
        continue

    match opcao:
        case 1:
            print(f"Seu saldo é: {saldo:.2f}")

        case 2: 
            while True:
                try:
                    deposito = float(input("Informe o valor que deseja depositar: "))
                except ValueError:
                    print("ERRO! Você deve informar números inteiros ou decimais (separando as casas decimais por ponto). Tente novamente.")
                    continue

                if deposito <= 0: 
                    print("ERRO! Você deve depositar um valor maior que zero. Tente novamente.")
                    continue
                else:
                    saldo += deposito
                    print(f"Depósito realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")
                    break
        
        case 3:
            while True:
                try:
                    saque = float(input("Informe o valor que deseja sacar: "))
                except ValueError:
                    print("ERRO! Você deve informar números inteiros ou decimais (separando as casas decimais por ponto). Tente novamente.")
                    continue

                if saldo <= 0:
                    print("ERRO! Você está liso. Arrume dinheiro para poder sacar alguma coisa.")
                    break

                if saque <= 0:
                    print("ERRO! Você deve sacar um valor maior que zero. Tente novamente.")
                    continue

                if saque > saldo:
                    print("ERRO! Você não tem todo esse dinheiro. Tente novamente.")
                    continue
                else:
                    saldo -= saque
                    print(f"Saque realizado com sucesso! Seu saldo atual é R$ {saldo:.2f}")

        case 4: 
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Tente novamente.")