"""
Faça um programa que leia tres numeros inteiro positivos e efetuo o calculo de uma das seguintes
medias de acordo com um valor numerico digitado pelo usuario:
(A) Geometrica: ³raiz X * Y * Z
(B) Ponderada: X + 2 * Y +3 * Z
                --------------
                        6
(C) Harmonica:      1
                ----------
                1 + 1 + 1
                -   -   -
                X   Y   Z

(D) Aritmetica: X + Y + Z
                ---------
                    3
"""

x = int(input("Informe um numero inteiro:"))
y = int(input("Informe um numero inteiro:"))
z = int(input("Informe um numero inteiro:"))

print("(A) Gemometrica \n"
      "(B) Ponderada \n"
      "(C) Harmonica \n"
      "(D) Aritimetica\n")
opcao = str(input("Escolha uma das opções:"))


def medias():
    if opcao == 'a' or opcao == 'A':
        geometrica = (x * y * z) ** (1/3)
        print("A media geometrica é {:.2f}".format(geometrica))
    elif opcao == 'b' or opcao == 'B':
        ponderada = (x + 2 * y + 3 * z) / 6
        print("A media geometrica é {:.2f}".format(ponderada))
    elif opcao == 'c' or opcao == 'C':
        harmonica = 1 / (1 / x + 1 / y + 1 / z)
        print("A media geometrica é {:.2f}".format(harmonica))
    elif opcao == 'd' or opcao == 'D':
        aritimetica = (x + y + z) / 3
        print("A media geometrica é {:.2f}".format(aritimetica))
    else:
        print("Opção Invalida!")


medias()
