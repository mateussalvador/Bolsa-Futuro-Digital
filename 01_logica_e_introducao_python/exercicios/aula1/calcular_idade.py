# 3 - leia o ano de nascimento de uma pessoa e o ano atual. Com base nisso, deve calcular a idade da pessoa e informar se ela é maior de idade (18 anos ou mais) ou não.
ano_nascimento = int(input("Informe o seu ano de nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nascimento
menor = idade < 18

print("--- DADOS DO USUÁRIO ---")
print(f"Idade atual: {idade}")
print("Você é menor de idade." if menor else "Você é maior de idade.")