"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a media geral.
"""

v = []
x = 0
soma = 0

while x < 15:
    n = float(input('Informe a nota do aluno:'))
    x += 1
    v.append(n)
    soma += n

media = soma / 15
print(media)
