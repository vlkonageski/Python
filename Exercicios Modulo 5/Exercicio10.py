"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
utilizando as seguintes formulas (onde H corresponde a altura):
º Homens: (72.7 * H) - 58
º Mulheres: (62.1 * H) - 44.7
"""

h = float(input("Informe sua altura:"))
sexo = str(input("Informe 'M' para masculino e 'F' para Feminino:"))


def peso_ideal():
    if sexo == 'm' or 'M':
        calculo = (72.7 * h) - 58
        print("Seu peso ideal é:{:.2f}".format(calculo))
    elif sexo == 'f' or 'F':
        calculo = (62.1 * h) - 44.7
        print("Seu peso ideal é:{:.2f}".format(calculo))


peso_ideal()
