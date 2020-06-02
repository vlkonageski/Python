"""
Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e imprima na saida cada 
um dos algarismos que compoem o numero.
"""

n = int(input('Informe um numero entre 100 e 999:'))

unidade = n % 10
dezena = int((n - unidade) / 10) % 10
centena = int((n - dezena) / 100)

print('Centena:', centena)
print('Dezena:', dezena)
print('Unidade:', unidade)
