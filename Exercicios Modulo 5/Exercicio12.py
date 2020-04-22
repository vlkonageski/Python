"""
Ler um numero inteiro. Se o numero lido for negativo, escreva a mensagem " numero invalido". Se o numero for positivo.
Calcular o logaritimo desse numero.
"""
import math

n = int(input("Informe um numero inteiro:"))


def logaritimo():
    try:
        if n >= 0:
            print("O logaritimo de", n, "é:", math.log(n))
        else:
            print("Numero Invalido!")
    except ValueError:
        print("Logaritimo de zero nao existe")


logaritimo()
