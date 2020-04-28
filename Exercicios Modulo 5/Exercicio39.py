"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo.
LEia o custo de fábrica e escreva o custo ao consumidor.
           ________________________________________________________________
          |      CUSTO DE FÁBRICA       |% DO DISTRIBUIDOR |% DOS IMPOSTOS|
          |---------------------------------------------------------------|
          |até R$12.000,00              |       5          |     isento   |
          |entre R$12.000,00 e 25.000,00|       10         |       15     |
          |acima de R$ 25.000,00        |       15         |       20     |
          |---------------------------------------------------------------|
"""

custo_fabrica = float(input("Informe o custo de fabrica do veiculo:"))


def custo_consumidor():
    if custo_fabrica <= 12000:
        custo = custo_fabrica + (custo_fabrica * 0.05)
        print("O custo do veiculo para o consumidor final é R${:.2f}".format(custo))
    elif custo_fabrica > 12000 and custo_fabrica <= 25000:
        custo = custo_fabrica + ( custo_fabrica * 0.10) + (custo_fabrica * 0.15)
        print("O custo do veiculo para o consumidor final é R${:.2f}".format(custo))
    else:
        custo = custo_fabrica + ( custo_fabrica * 0.15) + (custo_fabrica * 0.20)
        print("O custo do veiculo para o consumidor final é R${:.2f}".format(custo))


custo_consumidor()
