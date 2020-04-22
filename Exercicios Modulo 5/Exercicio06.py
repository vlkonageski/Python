"""
Escreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

n1 = int(input("Informe um numero inteiro:"))
n2 = int(input("Informe um numero inteiro:"))


def numeros():
    if n1 > n2:
        diferenca = n1 - n2
        print(n1, "É maior que", n2)
        print("A diferença entre eles é de:", diferenca)
    else:
        diferenca = n2 - n1
        print(n2, "É maior que", n1)
        print("A diferença entre eles é:", diferenca)


numeros()
