## 8 - leia a idade de duas pessoas e calcule a diferença de idade entre elas.
idade1 = int(input("Informe a idade da primeira pessoa: "))
idade2 = int(input("Informe a idade da segunda pessoa: "))
diferenca = (idade1 - idade2) if idade1 > idade2 else (idade2 - idade1)

print(f"A diferença entre as idades é: {diferenca}")
