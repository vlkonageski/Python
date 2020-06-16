"""
Chico tem 1.50 metros e cresce 2 centimetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centimetros por ano.
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""

altura_chico = 1.50
altura_ze = 1.10
anos = 0

while altura_ze < altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    anos += 1

print('Altura Chico = {:.2f}m'.format(altura_chico))
print('Altura Zé = {:.2f}m'.format(altura_ze))
print('Serão necessarios {} anos para Zé ficar mais alto que Chico.'.format(anos))
