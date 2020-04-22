"""
Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois numeros forem iguais,
imprima a mensagem numeros iguais.
"""

n1 = int(input("Informe um numero:"))
n2 = int(input("Informe um numero:"))


def maior_menor():
    if n1 > n2:
        print(n1, "É maior que", n2)
    elif n2 > n1:
        print(n2, "É maior que", n1)
    else:
        print("Numeros Iguais!")


maior_menor()
