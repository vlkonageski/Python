"""
Faça um programa que peça ao usuario para digitar 10 valores e some-os.
"""

x = 0
soma = 0
while x < 10:
    x += 1
    n = int(input("Informe um valor:"))
    soma += n

print("A soma dos valores é:", soma)
