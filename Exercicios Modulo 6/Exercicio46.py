"""
Faça um programa que gera um numero aleatorio de 1 a 1000. O usuario deve tentar acertar qual o numero foi 
gerado, a cada tentativa o programa deverá informar se o chute é menor, ou maior que o numero gerado. 
O programa acaba quando o usuario acertar o numero gerado. O programa deve informar em quantas tentativas 
o numero foi descoberto.
"""
from random import randint

n = int(randint(1, 1001))
y = 0

while True:
    x = int(input('Chute um numero:'))
    if x < n:
        print('O numero é maior!')
        y += 1
    elif x > n:
        print('O numero é menor!')
        y += 1
    else:
        print('Você acertou!')
        break

print('O numero era ', n)
print('Você acertou em {} tentativas.'.format(y))
