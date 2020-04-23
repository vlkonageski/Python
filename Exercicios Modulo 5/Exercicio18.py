"""
Faça um programa que mostre ao usuario um menu com 4 opções de operações matematicas
(as básicas, por exemplo).O usuário escolhe uma das opções e o seu programa entao pede dois valores
numéricos e realiza a operação, mostrando o resultado e saindo.
"""

print(  "1- Somar\n"
        "2- Subtrair\n"
        "3- Multiplicar\n"
        "4- Dividir")
opcao = int(input("Escolha uma opção:"))


def operacoes():
    if opcao == 1:
        n1 = float(input("Informe um valor:"))
        n2 = float(input("Informe um valor:"))
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    elif opcao == 2:
        n1 = float(input("Informe um valor:"))
        n2 = float(input("Informe um valor:"))
        subtracao = n1 - n2
        print(f"A subtração de {n1} - {n2} = {subtracao}")
    elif opcao == 3:
        n1 = float(input("Informe um valor:"))
        n2 = float(input("Informe um valor:"))
        multiplicacao = n1 * n2
        print(f"A multiplicação de {n1} * {n2} = {multiplicacao}")
    elif opcao == 4:
        n1 = float(input("Informe um valor:"))
        n2 = float(input("Informe um valor:"))
        divisao = n1 / n2
        print(f"A divisao de {n1} / {n2} = {divisao}")
    else:
        print("Opção Invalida!")


operacoes()
