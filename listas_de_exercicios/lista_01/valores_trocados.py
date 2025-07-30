# Faça um programa em Python que leia dois números inteiros quaisquer para as variáveis A e B, efetue a troca dos valores de forma que A passe a armazenar o valor de B e que B passe armazenar o valor de A e que imprima os valores trocados.

a = int(input("Digite o primeiro nṹmero: "))
b = int(input("Digite o segundo nṹmero: "))

a, b = b, a

print(f"Valor de a: {a}")
print(f"Valor de b: {b}")