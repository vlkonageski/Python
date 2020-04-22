"""
Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz quadrada do numero.
Se o numero for negativo, mostre uma mensagem dizendo que o numero é invalido.
"""
import math

n = int(input("Informe um numero positivo:"))


def raiz():
    if n >= 0:
        raiz_quadrada = math.sqrt(n)
        print("A raiz quadrada de", n, "é:", raiz_quadrada)
    else:
        print("Numero invalido!!!")


raiz()
