"""
Faça um programa que calcule a area de um triangulo, cuja base e altura sao fornecidas pelo usuario. 
Esse programa nao pode permitir a entrada de dados invalidos, ou seja, medidas menores ou iguais a 0.
"""

base = float(input('Informe a base do triangulo:'))
altura = float(input('Informe a altura do triangulo:'))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print('A area do traingulo é:', area)
else:
    print('Valores invalidos!')
