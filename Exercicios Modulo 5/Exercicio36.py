"""
Escreva um programa que, dado o valor da venda, imprima a comissao que deverá ser paga ao vendedor.
Para calcular a comissao, considere a tabela abaixo:
           _______________________________________________________________________________
          |                    VENDA MENSAL                     |      COMISSAO           |
          |-------------------------------------------------------------------------------|
          |Maior ou igual a R$100.000,00                        |R$700,00 + 16% das vendas|
          |Menor que R$100.000,00 e maior ou igual a R$80.000,00|R$650,00 + 14% das vendas|
          |Menor que R$80.000,00 e maior ou igual a R$60.000,00 |R$600,00 + 14% das vendas|
          |Menor que R$60.000,00 e maior ou igual a R$40.000,00 |R$550,00 + 14% das vendas|
          |Menor que R$40.000,00 e maior ou igual a R$20.000,00 |R$500,00 + 14% das vendas|
          |Menor que R$20.000,00                                |R$400,00 + 14% das vendas|
          |-------------------------------------------------------------------------------|
"""

vlr_venda = float(input("Informe o valor da venda:"))


def comissao():
    if vlr_venda >= 100.000:
        vlr_comissao = 700 + (vlr_venda * 0.16)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))
    elif vlr_venda < 100.000 and vlr_venda >= 80.000:
        vlr_comissao = 650 + ( vlr_venda * 0.14)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))
    elif vlr_venda < 80.000 and vlr_venda >= 60.000:
        vlr_comissao = 600 + ( vlr_venda * 0.14)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))
    elif vlr_venda < 60.000 and vlr_venda >= 40.000:
        vlr_comissao = 550 + ( vlr_venda * 0.14)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))
    elif vlr_venda < 40.000 and vlr_venda >= 20.000:
        vlr_comissao = 500 + ( vlr_venda * 0.14)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))
    else:
        vlr_comissao = 400 + ( vlr_venda * 0.14)
        print("A comissao do vendedor é R${:.2f}".format(vlr_comissao))


comissao()
