"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados
nas respectivas posições X e Y.
"""

v = [1, 2, 3, 4, 5, 6, 7, 8]
x = int(input('Informe um valor de 0 a 7:'))
y = int(input('Informe um valor de 0 a 7:'))

soma = v[x] + v[y]
print('A soma de {} + {} = {}'.format(v[x], v[y], soma))
