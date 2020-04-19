"""
Leia o salario de um funcionario. Calcule e imprima o valor do novo salario, sabendo que ele recebeu um aumento de 25%.
"""

slr_antigo = float(input("Informe o seu salario atual:"))
aumento = slr_antigo * 0.25

slr_novo = slr_antigo + aumento

print("Salario antigo:{:.2f}".format(slr_antigo))
print("Salario novo:{:.2f}".format(slr_novo))
