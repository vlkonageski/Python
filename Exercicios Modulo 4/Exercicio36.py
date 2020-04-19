"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
O volume de um cilindro circular é calculado por meio da seguinte formula V = pi * raio² * altura, onde pi = 3.141592
"""

pi = 3.141592

altura = float(input("Informe a altura:"))
raio = float(input("Informe o raio:"))

v = pi * (raio * raio) * altura

print("O volume do cilindro é:{:.2f}".format(v))
