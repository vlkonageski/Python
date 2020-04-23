"""
Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação esolhida.
Escreva uma mensagem de erro se a opção for invalida.
 1- Soma de dois numeros
 2- Diferença entre 2 numeros (maior pelo menor)
 3- Produto entre 2 numeros
 4- Divisao entre dois numeros (o denominador nao pode ser zero.)
 Opção
"""

print("1- Soma de dois numeros \n"
      "2- Diferença entre 2 numeros (maior pelo menor)\n"
      "3- Produto entre 2 numeros \n"
      "4- Divisao entre dois numeros (o denominador nao pode ser zero.)")

opcao = int(input("Informe a opção desejada:"))
    

def calcular():
    if opcao == 1:
        n1 = float(input("Informe um numero:"))
        n2 = float(input("Informe um numero:"))       
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    elif opcao == 2:
        n1 = float(input("Informe um numero:"))
        n2 = float(input("Informe um numero:"))
        if n1 > n2:       
            diferenca = n1 - n2
            print(f"A diferenca de {n1} - {n2} = {diferenca}")
        else:
            diferenca = n2 - n1
            print(f"A diferenca de {n2} - {n1} = {diferenca}")
    elif opcao == 3:
        n1 = float(input("Informe um numero:"))
        n2 = float(input("Informe um numero:"))       
        produto = n1 * n2
        print(f"O produto de {n1} * {n2} = {produto}")
    elif opcao == 4:
        n1 = float(input("Informe um numero:"))
        n2 = float(input("Informe um numero:"))
        if n2 > 0:       
            divisao = n1 / n2
            print(f"A divisao de {n1} / {n2} = {divisao}")
        else:
            print("O denominador deve ser maior que zero:")
    else:
        print("Opção invalida")


calcular()
