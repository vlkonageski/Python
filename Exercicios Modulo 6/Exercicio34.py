"""
Faça um programa que calcule o menor numero divisivel por cada um dos numeros de 1 a 20?
Ex: 2520 é o menor numero que pode ser dividido por cada um dos numeros de 1 a 10, sem sobrar resto.
"""

# importar o gcd da biblioteca math, ele calcula o mmc entre dois valores diferentes de zero.
from math import gcd

numeros = list(range(1, 21))
m = 1

for n in numeros:
    m = m * n // gcd(m, n)

print(m)
