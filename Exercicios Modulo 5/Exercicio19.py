"""
Faça um programa para verificar se um determinado numero é inteiro e divisivel por 3 ou 5,
mas nao simultaneamente pelos dois.
"""

n = float(input("Informe um numero:"))


def verificar():
    if(n // 1 == n): 
        if n % 3 == 0:
            print("O numero é inteiro e divisivel por 3")
        elif n % 5 == 0:
            print("O numero é inteiro e divisivel por 5")
        else:
            print("O numero é inteiro mas nao e divisivel por 3 nem por 5")
    else:
        print("O numero nao é inteiro")


verificar()
