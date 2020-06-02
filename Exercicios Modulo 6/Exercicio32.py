"""
Faça um programa que simula o lançamento de dois dados, D1 e D2, N vezes, e tem como saída o número de cada dado
e a relação entre eles (>,<,=) de cada lançamento.
"""
from random import randint

n = int(input('Informe quantas vezes quer jogar os dados:'))


for i in range(1, n+1):
    d1 = int(randint(1, 6))
    d2 = int(randint(1, 6))
    if d1 > d2:
        print('{} > {}'.format(d1, d2))
    elif d1 == d2:
        print('{} = {}'.format(d1, d2))
    else:
        print('{} < {}'.format(d1, d2))
