"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de imposto sobre o produto( MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuario entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado nao for valido, mostrar uma mensagem de erro.
"""

valor = float(input("Informe o valor do produto R$"))
estado = str(input("Informe o estado de destino:"))

def preco_final():
    if estado == 'mg' or estado == 'MG':
        imposto = valor * 0.07
        valor_final = valor + imposto
        print(f"O valor final do produto vendido para MG é R${valor_final}")
    elif estado == 'sp' or estado =='SP':
        imposto = valor * 0.12
        valor_final = valor + imposto
        print(f"O valor final do produto vendido para SP é R${valor_final}")
    elif estado == 'rj' or estado == 'RJ':
        imposto = valor * 0.15
        valor_final = valor + imposto
        print(f"O valor final do produto vendido para RJ é R${valor_final}")
    elif estado == 'ms' or estado == 'MS':
        imposto = valor * 0.08
        valor_final = valor + imposto
        print(f"O valor final do produto vendido para MS é R${valor_final}")
    else:
        print("Não vendemos para este estado!")


preco_final()
