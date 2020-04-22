"""
Escreva um programa que leia um numero inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao numero 251 corresponderá o valor 8 (2 + 5 + 1).
Se o numero lido nao for maior do que zero, o programa terminará com a mensagem "Numero inválido"
"""

numero = int(input("informe um numero maior que zero:"))
soma = 0
if numero > 0:
    while numero > 0:
        soma += numero % 10
        numero = numero // 10
    print(soma)
else:
    print("Numero Invalido!")
