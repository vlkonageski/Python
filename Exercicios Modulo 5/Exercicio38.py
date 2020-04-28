"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com um tabela que considera o salário atual
e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente
maior do que os funcionarios com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário 
irá receber um bonus adicional de salário. Faça um programa que leia:
    º O valor do salario atual do funcionário;
    º O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final
reajustado, ou uma mensagem caso o funcionário nao tenha direito a nenhum aumento.
           ___________________________________________________________
          | SALARIO ATUAL  | REAJUSTE(%)| TEMPO DE SERVIÇO | COMISSAO |
          |-----------------------------------------------------------|
          |Até 500,00      |     25%    | Abaixo de 1 ano  |Sem Bonus |
          |Até 1000,00     |     20%    | De 1 a 3 anos    |  100,00  |
          |Até 1500,00     |     15%    | De 4 a 6 anos    |  200,00  |
          |Até 2000,00     |     10%    | De 7 a 10 anos   |  300,00  |
          |Acima de 2000,00|Sem reajuste| Mais de 10 anos  |  500,00  |
          |-----------------------------------------------------------|
"""

salario_atual = float(input("Informe o salario atual do funcionario:"))
anos_servico = int(input("Informe a quantos anos o funcionario trabalha na empresa:"))


def aumento():
    if salario_atual <= 500:
        if anos_servico < 1:
            aumento = salario_atual + (salario_atual * 0.25)
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico >= 1 and anos_servico <= 3:
            aumento = salario_atual + (salario_atual * 0.25) + 100
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 3 and anos_servico <= 6:
            aumento = salario_atual + (salario_atual * 0.25) + 200
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 6 and anos_servico <= 10:
            aumento = salario_atual + (salario_atual * 0.25) + 300
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        else:
            aumento = salario_atual + (salario_atual * 0.25) + 500
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
    elif salario_atual > 500 and salario_atual <= 1000:
        if anos_servico < 1:
            aumento = salario_atual + (salario_atual * 0.20)
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico >= 1 and anos_servico <= 3:
            aumento = salario_atual + (salario_atual * 0.20) + 100
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 3 and anos_servico <= 6:
            aumento = salario_atual + (salario_atual * 0.20) + 200
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 6 and anos_servico <= 10:
            aumento = salario_atual + (salario_atual * 0.20) + 300
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        else:
            aumento = salario_atual + (salario_atual * 0.20) + 500
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
    elif salario_atual > 1000 and salario_atual <= 1500:
        if anos_servico < 1:
            aumento = salario_atual + (salario_atual * 0.15)
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico >= 1 and anos_servico <= 3:
            aumento = salario_atual + (salario_atual * 0.15) + 100
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 3 and anos_servico <= 6:
            aumento = salario_atual + (salario_atual * 0.15) + 200
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 6 and anos_servico <= 10:
            aumento = salario_atual + (salario_atual * 0.15) + 300
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        else:
            aumento = salario_atual + (salario_atual * 0.15) + 500
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
    elif salario_atual > 1500 and salario_atual <= 2000:
        if anos_servico < 1:
            aumento = salario_atual + (salario_atual * 0.10)
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico >= 1 and anos_servico <= 3:
            aumento = salario_atual + (salario_atual * 0.10) + 100
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 3 and anos_servico <= 6:
            aumento = salario_atual + (salario_atual * 0.10) + 200
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 6 and anos_servico <= 10:
            aumento = salario_atual + (salario_atual * 0.10) + 300
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        else:
            aumento = salario_atual + (salario_atual * 0.10) + 500
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
    elif salario_atual > 200:
        if anos_servico < 1:
            aumento = salario_atual
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico >= 1 and anos_servico <= 3:
            aumento = salario_atual + 100
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 3 and anos_servico <= 6:
            aumento = salario_atual + 200
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        elif anos_servico > 6 and anos_servico <= 10:
            aumento = salario_atual + 300
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
        else:
            aumento = salario_atual + 500
            print("O novo salario do funcionario será R${:.2f}".format(aumento))
    else:
        print("Não tem direito a aumento")


aumento()
