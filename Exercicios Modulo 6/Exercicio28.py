"""
Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme a formula a seguir
                    E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!
"""

n = int(input('Informe um numero:'))
e = 0

for i in range (1, n+1):
    e += 1/i

print('O valor de E:{:.2f}'.format(e))
