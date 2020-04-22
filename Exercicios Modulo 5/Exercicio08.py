"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas sao validas e exiba na tela a media destas notas.
Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota nao possua um valor valido,
este fato deve ser informado ao usuario e o programa termina
"""

n1 = float(input("Informe uma nota:"))
n2 = float(input("Informe uma nota:"))


def notas():
    if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:
        media = (n1 + n2) / 2
        print("A media das notas é:", media)
    else:
        print("Nota invalida:")
        exit(0)


notas()
