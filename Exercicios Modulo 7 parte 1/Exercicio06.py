"""
Faça um programa que receba do usuario um vetor de 10 posições. Em seguida deverá ser impresso o maior 
e o menor elemento do vetor.
"""

v = []
x = 0

while x < 10:
    n = int(input('Informe um valor:'))
    x += 1
    v.append(n)

print(v)
print('O maior numero do vetor é:', max(v))
print('O menor numero do vetor é:', min(v))
