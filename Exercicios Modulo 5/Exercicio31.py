"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir,
verifique e mostra qual a classificação dessa pessoa.
            ____________________________________________________________
          |  ALTURA      |                   PESO                       |
          |              |ate 60 | Entre 60 e 90(inclusive)| Acima de 90|
          | ------------------------------------------------------------|
          |menor que 1,20|   A   |            D            |      G     |
          |de 1,20 a 1,70|   B   |            E            |      H     |
          |maior que 1,70|   C   |            F            |      I     |
          |-------------------------------------------------------------|
"""

altura = float(input("Informe sua altura:"))
peso = float(input("Informe seu peso:"))


def classificacao():
    if altura < 1.20:
        if peso < 60:
            print("A")
        elif peso >= 60 and peso <= 90:
            print("D")
        else:
            print("G")
    elif altura >= 1.20 and altura <= 1.70:
        if peso < 60:
            print("B")
        elif peso >= 60 and peso <= 90:
            print("E")
        else:
            print("H")
    else:
        if peso < 60:
            print("C")
        elif peso >= 60 and peso <= 90:
            print("F")
        else:
            print("I")


classificacao()
            