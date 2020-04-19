"""
A importancia de R$780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
º O primeiro ganhador recebera 46%
º O segundo receberá 32%
º O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premio = 780000

g1 = premio * 0.46
g2 = premio * 0.32
g3 = premio - g1 - g2

print("Valor do Premio: R${:.2f}".format(premio))
print("Primeiro Ganhador: R${:.2f}".format(g1))
print("Segundo Ganhador: R${:.2f}".format(g2))
print("Terceiro Ganhador: R${:.2f}".format(g3))
