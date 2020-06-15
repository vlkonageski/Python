"""
Faça um algoritimo que converta uma velocidade expressa em km/h para m/s e vice versa. Você deve criar um menu
de opções de conversao e com uma opção para finalizar o programa. O usuario poderá fazer quantas conversoes
desejar, sendo que o programa só será finalizado quando a opção de finalizar for escolhida.
"""

while True:
    print('Escolha a opção desejada: \n'
    '1 - km/h -> m/s \n'
    '2 - m/s -> km/h \n'
    '3 - Finalizar Programa')
    opcao = int(input('Informe a opção desejada:'))
    if opcao == 1:
        km = float(input('Informe a velocidade em Km/h:'))
        conversao = km / 3.6
        print('{:.2f} m/s'.format(conversao))
    elif opcao == 2:
        ms = float(input('Informe a velocidade em m/s:'))
        conversao = ms * 3.6
        print('{:.2f} km/h'.format(conversao))
    elif opcao == 3:
        print('Programa Finalizado')
        break
    else:
        print('Digite uma opção valida!')
