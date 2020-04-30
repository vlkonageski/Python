"""
Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
"""

x = 0
n = 0
soma = 0

while n < 50:
    x += 1
    if x % 2 == 0:
        n += 1
        soma += x
    else:
        n = n

print("A soma dos 50 primeiros numeros pares é:", soma)