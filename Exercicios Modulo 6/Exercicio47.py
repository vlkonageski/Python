"""
Faça um programa que apresente um menu de opções para o calculo das seguintes operaçoes entre dois numeros:
ª adição (opção 1)
ª subtração (opção 2)
ª multiplicação (opção 3)
ª divisão (opção 4)
ª saída (opção 5)
O programa deve possibilitar ao usuario a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções.
O programa só termina quando for escolhida a opção de saída (opção 5).
"""


while True:
    print('Menu de Opcoes\n'
    '1 - Adicao\n'
    '2 - Subtracao\n'
    '3 - Multiplicacao\n'
    '4 - Divisao\n'
    '5 - Sair')
    opcao = int(input('Informe a opcao desejada:'))
    
    if opcao == 1:
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
        soma = n1 + n2
        print('A Soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
        subtracao = n1 - n2
        print('A Subtracao de {} - {} = {}'.format(n1, n2, subtracao))
    elif opcao == 3:
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
        multiplicacao = n1 * n2
        print('A Multiplicacao de {} * {} = {}'.format(n1, n2, multiplicacao))
    elif opcao == 4:
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
        divisao = n1 / n2
        print('A Divisao de {} / {} = {}'.format(n1, n2, divisao))
    elif opcao == 5:
        print('Programa Finalizado!')
        break
    else:
        print('Opcao Invalida!')
    