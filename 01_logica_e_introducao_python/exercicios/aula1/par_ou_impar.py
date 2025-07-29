# 2 - solicite ao usuário 1 numero e informe se este é par ou ímpar.

numero = int(input("Informe um número para verificar se é ímpar ou par: "))
resultado = "Par" if numero % 2 == 0 else "Ímpar"
print(f"O número é {resultado}")