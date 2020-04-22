"""
Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contratio imprima o numero ao quadrado.
"""
import math

n = float(input("Informe um numero real:"))


def numero():
    if n >= 0:
        raiz_quadrada = math.sqrt(n)
        print("A raiz quadrada de", n, "é:", raiz_quadrada)
    else:
        quadrado = n ** 2
        print("O quadrado de", n, "é:", quadrado)


numero()
