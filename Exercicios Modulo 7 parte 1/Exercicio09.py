"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem 
inversa.
"""

v = []
x = 0

while x < 6:
    n = int(input('Informe um numero par:'))
    if n % 2 == 0:
        x += 1
        v.append(n)
    else:
        print('Numero nao é par!')

print(v)
v.reverse()
print(v)
