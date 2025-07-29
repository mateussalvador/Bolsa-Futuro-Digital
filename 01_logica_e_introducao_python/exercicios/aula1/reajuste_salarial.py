# 7 - leia o salário atual de um funcionário e o percentual de reajuste, calcular e exibir o novo salário após o aumento.

salario_atual = float(input("Informe o seu salário atual: "))
reajuste = float(input("Qual o percentual (%) do reajuste? Informe apenas o número: "))
novo_salario = (salario_atual + (salario_atual * (reajuste / 100)))

print(f"O novo salário será de: R$ {novo_salario:.2f}")