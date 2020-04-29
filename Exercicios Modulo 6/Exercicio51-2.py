"""
Um funcionario recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu um aumento de 1.5%. A partir
de 1997, os aumentos sempre corresponderam ao dobro do ano anterior.
Faça um programa que determine o salario atual do funcionario.
"""

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

anoInicio = 1995
salarioInicial = 2000
porcent = 0.015
ano = int(input('Informe o ano atual:'))
novoSalario = 0

while anoInicio != ano:
    if anoInicio <= ano:
        anoInicio = anoInicio + 1
        if anoInicio == 1996:
            aumento = salarioInicial * porcent
            salarioFinal = salarioInicial + aumento
            print(end='Em {} o seu salario foi '.format(anoInicio))
            print(locale.currency(salarioFinal, grouping=True))
        else:
            salarioFinal += salarioFinal
            print(end='Em {} o seu salario foi '.format(anoInicio))
            print(locale.currency(salarioFinal, grouping=True))
    else:
        break
