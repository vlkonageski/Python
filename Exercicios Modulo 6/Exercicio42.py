"""
Faça um programa que leia um conjunto nao determinado de valores, um de cada vez, e escreva para cada um dos
valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""
import math

while True:
    n = int(input('Informe um numero inteiro:'))
    if n > 0:
        print('O quadrado de {} é = {}'.format(n, n**2))
        print('O cubo de {} é = {}'.format(n, n**3))
        print('A raiz quadrada de {} é = {:.2f}'.format(n, math.sqrt(n)))
    else:
        print('Programa Finalizado!')
        break
