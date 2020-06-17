"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = 0

for x in v:
    if x % 2 == 0:
        par += 1
    
print('O vetor possui {} valores pares.'.format(par))
