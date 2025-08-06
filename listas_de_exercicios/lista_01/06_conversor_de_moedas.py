#Crie um programa em Python que recebe um valor em reais e o converte para outra moeda. Use um menu para escolher a moeda de destino:
#1. Dólar
#2. Euro
#3. Libra
#4. Iene

#O programa deve perguntar o valor em reais e exibir o valor convertido para a moeda escolhida. Use valores fictícios para as taxas de conversão:

# 1 Real = 0.19 Dólar
# 1 Real = 0.17 Euro
# 1 Real = 0.15 Libra
# 1 Real = 25 Ienes

# Dicionário com os valores e opções para conversão
dicionario = {
    1: (0.19, "Dólar"),
    2: (0.17, "Euro"),
    3: (0.15, "Libra"),
    4: (25, "Iene"),
}

# Função que mostra o menu
def menu():
    print("---- CONVERSOR DE MOEDAS ----\n")
    print("Converte um valor em reais para a moeda desejada")
    print("1. Dólar")
    print("2. Euro")
    print("3. Libra")
    print("4. Iene")

def le_e_valida_valores():
    while True:
        menu()
        try:
            opcao = int(input("Informe a opção da moeda para a qual deseja converter: "))
            
            if opcao < 1 or opcao > 4:
                raise ValueError("Opção Inválida.")
            
            valor_em_reais = float(input("Informe o valor em reais que deseja converter: "))

            return (opcao, valor_em_reais)
        
        except (TypeError, ValueError):
            print("Entrada inválida. Tente novamente.")
            continue

def converte_valores(opcao_desejada, valor_em_reais):

    return valor_em_reais * dicionario[opcao_desejada][0]

if __name__ == "__main__":

    opcao_valor = le_e_valida_valores()
    opcao_desejada = opcao_valor[0]
    valor_em_reais = opcao_valor[1]
    valor_convertido = converte_valores(opcao_desejada, valor_em_reais)

    print(f"R$ {valor_em_reais:.2f} equivalem a {valor_convertido:.2f} em {dicionario[opcao_desejada][1]}.")