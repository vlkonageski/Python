"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

v = []
n = 0

while n < 6:
    numero = int(input('Informe um numero inteiro par:'))
    if numero % 2 == 0:
        n = n + 1
        v.append(numero)
    else:
        print('Informe um numero inteiro par!')

print(v)
v.reverse()
print(v)
