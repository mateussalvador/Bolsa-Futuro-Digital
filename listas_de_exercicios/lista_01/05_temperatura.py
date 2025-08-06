# Faça um programa em Python que leia a temperatura em graus Celsius e determine a classificação da temperatura:

#    • Menor que 0°C: Frio extremo
#    • De 0°C a 10°C: Frio
#    • De 11°C a 25°C: Ameno
#    • De 26°C a 35°C: Quente
#    • Maior que 35°C: Muito quente


def recebe_temperatura():
    temperatura = input("Informe a temperatura em graus Celsius (Cº): ")
    return temperatura

def le_e_valida_temperatura():
    while True:
        try:
            temperatura = float(recebe_temperatura())
            return temperatura
        except ValueError:
            print("Valor inválido para temperatura. Tente novamente.")

def classifica_temperatura(temperatura):

    if temperatura < 0:
        return "Frio extremo"
    elif temperatura <= 10:
        return "Frio"
    elif temperatura <= 25:
        return "Ameno"
    elif temperatura <= 35:
        return "Quente"
    else:
        return "Muito quente"

if __name__ == "__main__":
    temperatura = le_e_valida_temperatura()
    classificacao = classifica_temperatura(temperatura)
    print(f"A temperatura de {temperatura:.2f} ºC é classificada como {classificacao}")
        