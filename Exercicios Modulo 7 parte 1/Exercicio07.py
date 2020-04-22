"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição
que ele se encontra.
"""

v = []
n = 0

while n < 10:
    n = n + 1
    numero = int(input("Informe um numero inteiro: "))
    v.append(numero)

print(v)
print(f'O maior emlemento do vetor é {max(v)}')
print(f'O maior elemento se encontra na posição {v.index(max(v))}')
