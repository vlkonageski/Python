"""
Leia um vetor de 20 numeros inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
"""

v = [1, 2, 3, 4, 5, 6, 7, 2, 3, 10, 5, 6, 7, 9, 10, 7, 6, 2, 1, 4]
print(v)

for x in v:
    if v.count(x) > 1:
        v.remove(x)

print(v)