"""
Leia quatro notas, calcule a média aritmetica e imprima o resultado.
"""

n1 = float(input("Informe a primeira nota:"))
n2 = float(input("Informe a segunda nota:"))
n3 = float(input("Informe a terceira nota:"))
n4 = float(input("Informe a quarta nota:"))

media = (n1 + n2 + n3 + n4) / 4

print("A media das notas é:{:.2f}".format(media))
