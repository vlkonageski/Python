"""
Faça um programa que leia um numero inteiro positivo N e calcule a soma dos N primeiros numeros naturais.
"""

n = int(input("Informe um numero inteiro:"))
x = 0
soma = 0

while x <= n:
    soma += x
    x += 1

print(soma)
