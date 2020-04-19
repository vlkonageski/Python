"""
Faca um programa que leia o valor da hora de trabalho (em reais) e numeros de horas trabalhadas no mes.
Imprima o valor a ser pago ao funcionario, adicionado 10% sobre o valor do calculo.
"""

vlr_hora = float(input("Informe o valor da hora trabalhada:"))
horas = float(input("Informe a quantidade de horas trabalhadas no mes:"))
adicional = (vlr_hora * horas) * 0.10
receber = (vlr_hora * horas) + adicional

print("O valor total a receber é: R${:.2f}".format(receber))
