"""
Faça um algoritmo que encontre os multiplos de 11, 13 ou 17 apos um numero dado.
"""

n = int(input('Informe um numero:'))

for i in range(1, n+1):
    if i % 11 == 0:
        print('{} é multiplo de 11.'.format(i))
    elif i % 13 == 0:
        print('{} é multiplo de 13.'.format(i))
    elif i % 17 == 0:
        print('{} é multiplo de 17.'.format(i))
