"""
Leia um valor em real e a cotação do dolar. Em seguida, imprima o valor correspondente em dólares.
"""

real = float(input("Informe o valor em R$:"))
cotacao = float(input("Informe o valor da cotacao do Dolar:"))

dolar = real * cotacao

print("Real:{:.2f}".format(real))
print("Dolar:{:.2f}".format(dolar))
