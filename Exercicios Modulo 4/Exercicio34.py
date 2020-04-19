"""
Leia o valor do raio de um circulo e clacule e imprima a area do circulo correspondente.
A area do circulo é pi * raio², considere pi = 3.141592
"""

pi = 3.141592
raio = float(input("Informe o raio do circulo:"))

area = pi * (raio * raio)

print("A area do circulo é:{:.2f}".format(area))
