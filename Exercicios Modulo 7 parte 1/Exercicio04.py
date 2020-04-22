"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes
a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.
"""

v = []
n = 0

while n < 10:
    n = n + 1
    numero = int(input("Informe um numero:"))
    v.append(numero)
x = int(input("Informe um valor de 0 a 7:"))
y = int(input("Informe um valor de 0 a 7"))

soma = v[x] + v[y]

print(v)
print(f'A soma de {v[x]} + {v[y]} = {soma}')
