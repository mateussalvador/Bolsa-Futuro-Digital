# Elabore um programa em Python que leia as duas notas de prova (P1 e P2) e duas notas de trabalho (T1 e T2) e posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não aprovado’ dependendo dos valores obtidos, conforme as regras de cálculo definidas a seguir:

#   • Média de provas: MP = (P1 + P2)/2
#    • Média de trabalhos: MT = (T1 + T2)/2
#    • Média final: MF = 0,8MP + 0,2MT
#    • Situação:
#        ◦ Se MF ≥ 6,0 → aprovado
#        ◦ Se MF < 6,0 → não aprovado

media_final = 0

def recebe_nota(nome_da_nota):
    while True: 
        try:
            nota = float(input(f"Informe a nota do(a) {nome_da_nota}: "))
            return nota

        except ValueError:
            print("Erro! Insira apenas valores numéricos. Tente novamente!")
            continue

def calcula_media():

    p1 = recebe_nota("Prova 1")
    p2 = recebe_nota("Prova 2")
    t1 = recebe_nota("Trabalho 1")
    t2 = recebe_nota("Trabalho 2")

    media_provas = (p1 + p2) / 2
    media_trabalhos = (t1 + t2) / 2
    media_final = media_provas * 0.8 + media_trabalhos * 0.2

    return media_final

def verifica_resultado(media_final):
    if media_final < 6:
        return "Não Aprovado!"
    else:
        return "Aprovado!"
    
if __name__ == "__main__":
    media_final_do_aluno = calcula_media()
    print(f"A sua média final foi: {media_final_do_aluno:.2f}. Seu resultado final é: {verifica_resultado(media_final_do_aluno)}")