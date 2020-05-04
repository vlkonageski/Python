"""
Faça um programa que leia um numero inteiro positivo par N e imprima todos os numeros pares de 0 ate N
em ordem crescente.
"""

n = int(input("Informe um numero inteiro:"))
x = 0

while x <= n:
    if x % 2 == 0:
        print(x)
        x += 1
    else:
        x += 1
