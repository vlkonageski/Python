"""
Faça um programa que leia um numero inteiro positivo N e imprima todos os numeros naturais de 0 ate N
em ordem decrescente.
"""

n = int(input("Informe um numero inteiro:"))
x = 0

while n >= 0:
    print(n)
    n -= 1
    
