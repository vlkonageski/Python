"""
Leia a distancia em KM e a quantidade de litros de gasolina consumidos por um carro em um percurso, 
calcule o consumo em KM/L e escreva uma mensagem de acordo com a tabela abaixo
            __________________________________
          |  CONSUMO |(KM/L) |  MENSAGEM       |
          | ---------------------------------- |
          | menor que| 8     | Venda o Carro!  |
          | entre    | 8 e 14| Economico!      |
          | maior que| 14    | Super Economico!|
          |----------------------------------- |
"""

km = float(input("Informe a distancia em km percorrida:"))
qtd_litros = float(input("Informe a quantidade de litros de gasolina consumidos:"))
consumo = km / qtd_litros

def calculo():
    if consumo < 8:
        print("A media de consumo do carro é {:.2f} km/l".format(consumo))
        print("Venda o Carro!")
    elif consumo >= 8 and consumo <= 14:
        print("A media de consumo do carro é {:.2f} km/l".format(consumo))
        print("Economico!")
    else:
        print("A media de consumo do carro é {:.2f} km/l".format(consumo))
        print("Super Economico!")


calculo()
