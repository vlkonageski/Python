"""
Faça um programa que some todos os numeros naturais abaixo de 1000 que sao multiplos de 3 ou 5.
"""

soma = 0

for i in range (1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        soma += i
        print(i)

print('A soma de todos os numeros naturais abaixo de 1000 que sao multiplos de 3 ou 5 =', soma)