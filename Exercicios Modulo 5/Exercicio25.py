"""
Calcule as raizes da equação de 2º grau.
            Lembrando que:
            x = -b+- raiz delta
                ---------------
                    2a
                    Onde
                delta = B² - 4ac

E ax² + bx + c = ) representa uma equação de 2º grau.
A variavel A tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
 ºSe delta < 0, nao existe real. Imprima a mensagem "Nao existe raiz"
 ºSe delta = 0, existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
 ºSe delta >= 0, imprima as duas raizes reais.
"""

a = float(input("Informe o valor de A:"))
b = float(input("Informe o valor de B:"))
c = float(input("Informe o valor de C:"))
delta = (b ** 2) - (4 * a * c)
raiz_delta = delta ** 0.5

def equacao():
    if a == 0:
        print("Não é uma equação de segundo grau!")
    elif delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        print("Raiz Unica")
    elif delta >= 0:
        raiz_a = (-b + raiz_delta) / (2 * a)
        raiz_b = (-b - raiz_delta) / (2 * a)
        print(f"x1 é igual a: {raiz_a}")
        print(f"x2 é igual a: {raiz_b}")


equacao()
