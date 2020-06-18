"""
Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene em um vetor com 10 posições.
Preencha um segundo vetor apenas com os números impares do primeiro vetor. 
Imprima os dois vetores, 2 elementos por linha.
"""

from random import randint

v = []
v2 = []

for x in range(10):
    n = randint(0, 50)
    v.append(n)
    if n % 2 != 0:
        v2.append(n)

print(v)
print(v2)
