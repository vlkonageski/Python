"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

v = []
n = 0
par = 0

while n < 10:
    n = n + 1
    numero = int(input("Informe um numero:"))
    v.append(numero)
    if numero % 2 == 0:
       par = par + 1

print(v)
print(f'O vetor possui {par} numeros pares')
