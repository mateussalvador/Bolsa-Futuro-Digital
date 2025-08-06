# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e
# informe o tempo aproximado de download do arquivo usando este link (em minutos).

import decimal
import sys

def calcular_tempo_download():
    try:
        tamanho_arquivo_mb = input("Informe o tamanho do arquivo para download (em MB): ")
        velocidade_mbps = input("Informe a velocidade do link de internet (em Mbps): ")

        tamanho_arquivo_mb = decimal.Decimal(tamanho_arquivo_mb)
        velocidade_mbps = decimal.Decimal(velocidade_mbps)

        if tamanho_arquivo_mb < 0 or velocidade_mbps <= 0:
            print("Erro: O tamanho do arquivo deve ser positivo e a velocidade da internet deve ser maior que zero.")
            sys.exit()

    except decimal.InvalidOperation:
        print("Erro: Entrada inválida. Por favor, digite apenas números para o tamanho do arquivo e a velocidade da internet.")
        sys.exit()
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit()

    # 1 MB (MegaByte) = 8 Mb (Megabits)
    # Convertemos o tamanho do arquivo de MegaBytes para MegaBits para que as unidades sejam compatíveis com Mbps.
    tamanho_arquivo_megabits = tamanho_arquivo_mb * 8

    # O tempo é calculado dividindo o tamanho do arquivo (em MegaBits) pela velocidade (em MegaBits por segundo)
    tempo_total_segundos = tamanho_arquivo_megabits / velocidade_mbps

    # Calcula os minutos e segundos
    minutos = int(tempo_total_segundos // 60)
    segundos = int(tempo_total_segundos % 60)
    
    # Se você quiser maior precisão, pode mostrar os segundos com casas decimais:
    # segundos_com_decimal = tempo_total_segundos % 60
    # print(f"O tempo aproximado para download do arquivo será de {minutos} minutos e {segundos_com_decimal:.2f} segundos")

    if minutos > 1:
        print(f"\nO tempo aproximado para download do arquivo será de {minutos} minutos e {segundos} segundos.")
    
    if minutos == 0:
        print(f"\nO tempo aproximado para download do arquivo será de {segundos} segundos.")
    
    if minutos == 1: 
        print(f"\nO tempo aproximado para download do arquivo será de 1 minuto e {segundos} segundos.")

if __name__ == "__main__":
    calcular_tempo_download()