"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuirem valores negativos.
"""

v = []
for i in range(10):
    n = int(input('Digite um numero:'))
    v.append(n)
print(v)

for i in range(10):
    if v[i] < 0:
        v[i] = 0
print(v)
