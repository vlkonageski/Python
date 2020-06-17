"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento
e a posição que ele se encontra.
"""

v = []
x = 0

while x < 10:
    n = int(input('Informe um numero:'))
    x += 1
    v.append(n)

print(v)
print('O maior elemento da lista é:', max(v))
print('O maior elemento da lista se encontra na posição:', v.index(max(v)))
