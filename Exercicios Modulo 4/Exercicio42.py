"""
Receba o salario-base de um funcionario. Calcule e imprima o salario a receber, sabendo-se que esse funcionario tem
uma gratificacao de 5% sobre o salario-base. Alem disso, ele paga 7% de imposto sobre o salario-base.
"""

salario_base = float(input("Informe o salario base:"))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07

receber = salario_base + gratificacao - imposto

print("Salario Base: R${:.2f}".format(salario_base))
print("Salario a receber: R${:.2f}".format(receber))
