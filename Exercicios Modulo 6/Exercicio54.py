"""
Faça um programa que receba um numero inteiro maior do que 1, e verifique se o numero fornecido é primo ou nao.
"""

numero = int(input('Informe um numero:'))

for n in range(1, numero):
    cont = 0
    for x in range(1, numero + 1):
        if n % x == 0:
            cont += 1
    if cont <= 2:
        print('é primo')



