"""
A nota final de um estudante é calculada a partir de tres notas atribuidas entre o intervalo de 0 a 10,
respectivamente, a um trabalho de laboratorio, a uma avaliação semestral e a um exame final. 
A media dos três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratorio: 2; 
Avaliação semestral: 3; Exame final: 5; De acordo com o resultado, mostre na tela se o aluno 
esta reprovado (media entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. 
Faça todas as verificaçlões necessarias.
"""

trabalho = float(input("Informe a nota do trabalho de laboratorio:"))
avaliacao = float(input("Informe a nota da Avaliacao Semestral:"))
exame = float(input("Informe a nota do Exame Final:"))


def media_aluno():
    media = ((trabalho * 2) + (avaliacao * 3) + (exame * 5)) / 10
    if media >= 0 and media <= 2.9:
        print(f"A media do aluno é {media}")
        print("Aluno Reprovado!")
    elif media >= 3 and media <= 4.9:
        print(f"A media do aluno é {media}")
        print("Aluno de Recuperação!")
    else:
        print(f"A media do aluno é {media}")
        print("Aluno Aprovado!")


media_aluno()
