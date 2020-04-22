"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação for maior que 20% do salario imprima.
Emprestimo nao concedido, caso contratio imprima: Emprestimo concedido.
"""

salario = float(input("Informe o salario do trabalhador:"))
prestacao = float(input("Informe o valor da prestação:"))
porcentagem = salario * 0.20


def emprestimo():
    if prestacao <= porcentagem:
        print("Emprestimo concedido!")
    else:
        print("Emprestimo nao concedido!")


emprestimo()
