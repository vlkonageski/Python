"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
"""

produto = float(input("Informe o valor do produto:"))
desconto = produto * 0.12

pagar = produto - desconto

print("O valor do produto sem desconto e de:{:.2f}".format(produto))
print("O valor a ser pago com desconto é{:.2f}".format(pagar))
