"""
Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores desses numeros,
com exceção dele proprio. Ex: a soma dos divisores do numero 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
"""

n = int(input('Informe um numero inteiro:'))
soma = 0

for i in range(1, n ):
    if n % i == 0:
        soma += i 
        print(i)        
print('A soma de todos os divisores de {} = {}'.format(n, soma))
