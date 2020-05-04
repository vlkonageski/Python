"""
Faça um programa que leia um numero inteiro positivo par N e imprima todos os numeros pares de 0 ate N
em ordem decrescente.
"""

n = int(input("Informe um numero inteiro:"))
x = 0

while n != 0:
    if n % 2 == 0:
        print(n)
        n -= 1
    else:
        n -= 1
