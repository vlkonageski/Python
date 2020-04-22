"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

v = []
n = 0

while n < 6:
    n = n + 1
    numero = int(input("Informe um numero inteiro: "))
    v.append(numero)

print(v)
v.reverse()
print(v)
