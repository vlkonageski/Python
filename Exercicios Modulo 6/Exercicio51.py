"""
Um funcionario recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu um aumento de 1.5%. 
A partir de 1997, os aumentos sempre corresponderam ao dobro do ano anterior.
Faça um programa que determine o salario atual do funcionario.
"""

ano_atual = int(input('Informe o ano atual:'))
salario_inicial = 2000
ano = 1996
aumento = 0.015
salario_atual = (salario_inicial * aumento) + salario_inicial

while ano <= ano_atual:
    print('Em {} o seu salario foi R${:000,.2f}'.format(ano, salario_atual))
    ano += 1
    aumento = aumento * 2
    salario_atual = (salario_inicial * aumento) + salario_atual
    