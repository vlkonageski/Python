"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne 
quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possivel. 
Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""

saque = int(input('Informe o valor do saque:'))

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0

print('Foram usadas para sacar o valor de R${}'.format(saque))
while True:
    if saque >= 100:
        notas100 += 1
        saque = saque - 100
    elif saque >= 50:
        notas50 += 1
        saque = saque - 50
    elif saque >= 20:
        notas20 += 1
        saque = saque - 20
    elif saque >= 10:
        notas10 += 1
        saque = saque - 10
    elif saque >= 5:
        notas5 += 1
        saque = saque - 5
    elif saque >= 2:
        notas2 += 1
        saque = saque - 2
    elif saque >= 1:
        notas1 += 1
        saque = saque - 1
    elif saque == 0:
        break

print('{} notas de R$100,00\n'
      '{} notas de R$50,00\n'
      '{} notas de R$20,00\n'
      '{} notas de R$10,00\n'
      '{} notas de R$5,00\n'
      '{} notas de R$2,00\n'
      '{} notas de R$1,00'
      .format(notas100, notas50, notas20, notas10, notas5, notas2, notas1))
