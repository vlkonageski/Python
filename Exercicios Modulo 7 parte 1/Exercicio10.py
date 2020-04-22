"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a media geral.
"""

v = []
n = 0

while n < 15:
    n = n + 1
    nota = float(input('Informe a nota do aluno:'))
    v.append(nota)

print(v)
# sum -> soma os valores dentro da lista
# len -> conta a quantidade de elementos dentro da lista
print('A media geral das notas é{: 0.2f}'.format(sum(v) / len(v)))
