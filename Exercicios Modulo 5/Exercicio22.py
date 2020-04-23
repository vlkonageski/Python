"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se aposentar.
As condições para aposentadoria sao.
 º Ter pelo menos 65 anos
 º Ou ter trabalhado pelo menos 30 anos
 º Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""

idade = int(input("Informe a sua idade:"))
servico = int(input("Informe quanto tempo de serviço:"))


def aposentadoria():
    if idade >= 65:
        print("Já pode se aposentar!")
    elif servico >= 30:
        print("Já pode se aposentar!")
    elif idade >= 60 and servico >= 25:
        print("Já pode se aposentar!")
    else:
        print("Não pode se aposentar!")


aposentadoria()
