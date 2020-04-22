"""
Faça um programa que leia um conjunto nao determinado de valores, um de cada vez, e escreva para cada um dos valores lidos,
o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""

n = 1

while n >= 1:
    n = int(input('Informe um numero:'))
    if n >= 1:
        quadrado = n * n
        cubo = n ** 3
        raiz = n ** (1/2)
        print('O quadrado de {} é:{}'.format(n,quadrado))
        print('O cubo de {} é:{}'.format(n,cubo))
        print('A raiz quadrada de {} é:{:00.2f}'.format(n,raiz))
    else:
        break
print('Programa Finalizado!')