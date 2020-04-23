"""
Determine se um determinado ano lido é bisexto. Sendo que um ano é bisexto se for divisivel por 400
ou se for divisivel por 4 e nao for divisiel por 100. por exemplo 1988, 1992, 1996.
"""

ano = int(input("Informe o ano:"))


def bisexto():
    if ano % 400 == 0:
        print(f"{ano} é Bisexto!")
    elif ano % 4 == 0 and ano % 100 != 0:
        print(f"{ano} é Bisexto!")
    else:
        print(f"{ano} não é Bisexto!")


bisexto()
