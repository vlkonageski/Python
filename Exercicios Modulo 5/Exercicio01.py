"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

a = int(input("Informe o valor de A:"))
b = int(input("Informe o valor de B:"))


def maior():
    if a > b:
        print(a, "é maior que", b)
    elif b > a:
        print(b, "é maior que", a)
    else:
        print(a, " e ", b, "são iguais")


maior()
