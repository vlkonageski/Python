"""
Faça um algoritmo que leia um numero positivo e imprima seus divisores.
"""

n = int(input('Informe um numero intero positivo:'))

for i in range(1, n + 1):
    if n % i == 0:
        print('{} e divisivel por {}'.format(n, i))
