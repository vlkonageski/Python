"""
Escreva um programa para calcular o valor da serie, para 5 termos.
            S = 0 + 1/2! + 2/4! + 3/6 + ...
"""

soma = 0
n = 0

for i in range (1, 5):
    n += 2
    soma += i/n

print('A soma total da serie é:', int(soma))
