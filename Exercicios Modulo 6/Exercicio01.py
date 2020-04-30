"""
Faça um programa que determine e mostre os cinco primeiros multiplos de 3, considerando numeros maiores que 0.
"""
x = 0
n = 0


def multiplo():
    while x < 5:
        n += 1
        if n % 3 == 0:
            x += 1
            print(n)


multiplo()
