"""
Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""

a = int(input("Informe o valor de A:"))
b = int(input("Informe o valor de B:"))
c = int(input("Informe o valor de C:"))

resultado = (a * a) + (b * b) + (c * c)

print("Resultado:{:.2f}".format(resultado))
