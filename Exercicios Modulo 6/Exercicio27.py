"""
Em matematica, o numero harmonico designado por H(n) define-se como sendo a soma da serie harmonica:
                H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""

n = int(input('Informe um numero:'))
soma = 0

for i in range (1, n+1):
    soma += 1/i

print('A soma harmonica é:{:.2f}'.format(soma))
