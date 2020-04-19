"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o numero de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

vlr_diaria = 30
dias = int(input("Informe quantos dias forma trabalhados:"))
desconto = (vlr_diaria * dias) * 0.08
receber = (vlr_diaria * dias) - desconto

print("O encanador recebera com imposto descontado: R${:.2f}".format(receber))
