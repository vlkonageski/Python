"""
Faça um programa que receba tres numero e mostre-os em ordem crescente.
"""

n1 = int(input("Informe um numero:"))
n2 = int(input("Informe um numero:"))
n3 = int(input("Informe um numero:"))


def ordem():
    numeros = n1, n2, n3
    print(sorted(numeros))


ordem()
