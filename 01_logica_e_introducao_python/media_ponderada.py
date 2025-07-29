# 1 - solicite ao usuário o nome do estudante e 3 notas, retorne a média ponderada das notas (com pesos 1,1 e 2), o nome do estudante e se reprovado (media 6 aprovado).

PESO_1 = 1
PESO_2 = 1
PESO_3 = 2
SOMA_PESOS = PESO_1 + PESO_2 + PESO_3
nome = input("Informe o seu nome: ")
nota_1 = float(input("Informe a nota 1: "))
nota_2 = float(input("Informe a nota 2: "))
nota_3 = float(input("Informe a nota 3: "))
media_ponderada = ((nota_1 * PESO_1) + (nota_2 * PESO_2) + (nota_3 * PESO_3)) / SOMA_PESOS
aprovacao = "Reprovado" if media_ponderada < 6 else "Aprovado"

print("--- DADOS DO ALUNO ---")
print(f"Nome do Aluno: {nome}")
print(f"Média Ponderada: {media_ponderada:.2f}")
print(f"Aprovação: {aprovacao}")

