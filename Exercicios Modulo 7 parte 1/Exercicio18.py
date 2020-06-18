"""
Faça um programa que leia um vetor de 10 numeros. Leia um numero X. Conte os múltiplos de um numero inteiro X
num vetor e mostre-os na tela.
"""

v = []
for i in range(10):
    n = int(input('Digite um numero:'))
    v.append(n)
print(v)

mult = int(input('Informe um numero:'))
v2 = []
for i in range(10):
    if mult % v[i] == 0:
        v2.append(v[i])
print(v2)
