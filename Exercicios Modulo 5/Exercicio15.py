"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana
correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""

n = int(input("Informe um numero de 1 a 7:"))


def dias_semana():
    if n == 1:
        print("Domingo")
    elif n == 2:
        print("Segunda-Feira")
    elif n == 3:
        print("Terça-Feira")
    elif n == 4:
        print("Quarta-Feira")
    elif n == 5:
        print("Quinta-Feira")
    elif n == 6:
        print("Sexta-Feira")
    elif n == 7:
        print("Sábado")
    else:
        print("Numero Invalido")


dias_semana()
