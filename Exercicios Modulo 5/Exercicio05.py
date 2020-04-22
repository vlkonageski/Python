"""
Faça um programa que receba um numero inteiro e verifique se este numero é par ou impar.
"""

n = int(input("Informe um numero:"))


def par_impar():
    if n % 2 == 0:
        print(n, "É par!")
    else:
        print(n, "É impar!")


par_impar()
