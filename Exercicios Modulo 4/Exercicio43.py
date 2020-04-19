"""
Escreva um programa de ajuda para vendedores. A partir de um valor lido, mostre:
* o total a pagar com desconto de 10%
* o valor de cada parcela, no parcelamento de 3x sem juros
* a comissao do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
* a comissao do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

valor = float(input("Informe o valor do produto:"))
desconto = valor - (valor * 0.10)
parcela = valor / 3
comissao_vista = desconto * 0.05
comissao_parcela = valor * 0.05

print("Valor do produto: R${:.2f}".format(valor))
print("Valor do produto a vista: R${:.2f}".format(desconto))
print("Valor das parcelas em 3x: R${:.2f}".format(parcela))
print("Comissao vendedor venda a vista: R${:.2f}".format(comissao_vista))
print("Comissao vendedor venda parcelada: R${:.2f}".format(comissao_parcela))
