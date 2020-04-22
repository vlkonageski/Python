"""
Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
º O numero digitado ao quadrado
º A raiz quadrada do numero digitado.
"""
import math

n = int(input("Informe um numero:"))


def numero():
    if n >= 0:
        quadrado = n ** 2
        raiz = math.sqrt(n)
        print("O quadrado de", n, "é:", quadrado)
        print("A raiz quadrada de", n, "é:", raiz)
    else:
        print("Numero invalido!")


numero()
