"""
Faça um programa que receba do usuario um vetor de 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.
"""

v = []
n = 0

while n < 10:
    n = n + 1
    numero = int(input("Informe um numero: "))
    v.append(numero)

print(v)
print(f'O maior número do vetor é {max(v)}')
print(f'O menor número do vetor é {min(v)}')
