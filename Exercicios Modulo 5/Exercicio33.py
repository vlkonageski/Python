"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva 
o preço novo, e escreva uma mensagem em função do preço novo ( de acordo com a segunda tabela).
            __________________________________
          |     PREÇO ANTIGO   |% DE AUMENTO  |
          | ----------------------------------|
          |até R$ 50           |     5%       |
          |entre R$ 50 e R$ 100|    10%       |
          |acima de R$ 100     |    15%       |
          |-----------------------------------|
            __________________________________
          |     PREÇO NOVO      | MENSAGEM    |
          | ----------------------------------|
          |até R$ 80            |   Barato    |
          |entre R$ 80 e R$ 120 |   Normal    |
          |entre R$ 120 e R$ 200|   Caro      |
          |acima de R$ 200      | Muito Caro  |
          |-----------------------------------|
"""

preco_antigo = float(input("Informe o preço antigo:"))


def tabela():
    if preco_antigo <= 50:
        aumento = preco_antigo + ( preco_antigo * 0.05)
        print(f"O novo valor é R${aumento}")
        if aumento <= 80:
            print("Barato")
        elif aumento > 80 and aumento <= 120:
            print("Normal")
        elif aumento > 120 and aumento <= 200:
            print("Caro")
        else:
            print("Muito Caro")
    elif preco_antigo > 50 and preco_antigo <= 100:
        aumento = preco_antigo + ( preco_antigo * 0.10)
        print(f"O novo valor é R${aumento}")
        if aumento <= 80:
            print("Barato")
        elif aumento > 80 and aumento <= 120:
            print("Normal")
        elif aumento > 120 and aumento <= 200:
            print("Caro")
        else:
            print("Muito Caro")
    else:
        aumento = preco_antigo + ( preco_antigo * 0.15)
        print(f"O novo valor é R${aumento}")
        if aumento <= 80:
            print("Barato")
        elif aumento > 80 and aumento <= 120:
            print("Normal")
        elif aumento > 120 and aumento <= 200:
            print("Caro")
        else:
            print("Muito Caro")


tabela()
