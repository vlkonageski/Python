"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

v = []
x = 0

while x < 6:
    n = int(input('Informe um numero:'))
    x += 1
    v.append(n)

print(v)
v.reverse()
print(v)
