"""
Faça um programa que leia um numero inteiro N e depois imprima os N primeiros numeros naturais impares.
"""

n = int(input("Informe um numero:"))
x = 0

while x != n:
    x +=1
    if x % 2 != 0:
        print(x)
    else:
        x = x
