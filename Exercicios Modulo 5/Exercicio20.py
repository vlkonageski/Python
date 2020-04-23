"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo e, se forem,
se é um triangulo escaleno, equilatero ou isoscele, considerando os seguintes conceitos.
 º O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
 º Chama-se equilatero o triangulo que tem tres lados iguais
 º Denomina-se isosceles o triangulo que tem o comprimento de dois lados iguais.
 º Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.
"""

a = float(input("Informe o valor de A:"))
b = float(input("Informe o valor de B:"))
c = float(input("Informe o valor de C:"))


def triangulos():
    if a < b + c or b < a + c or c < a + b:
        print("Pode ser um triangulo")
        if a == b and a == c and b == c:
            print("Triangulo Equilatero")
        elif a == b or a == c or b == c:
            print("Triangulo Isosceles")
        else:
            print("Triangulo Escaleno")
    else:
        print("Não pode ser um triangulo")


triangulos()
