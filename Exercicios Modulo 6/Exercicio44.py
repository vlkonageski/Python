"""
Leia um numero positivo do usuario, entao, calcule e imprima a sequencia Fibonacci ate o primeiro numero 
superior ao numero lido.
Exemplo: se o usuario informou o numero 30, a sequencia a ser impressa sera 0 1 2 3 5 8 13 21 34.
"""

n = int(input('Informe um numero inteiro: '))
prox = 0
ant = 0
lista = []

while True:
    print(prox)
    prox = prox + ant
    ant = prox - ant
    if prox == 0:
        prox += 1 
    elif prox > n:
        print(prox)
        break
