"""
Ler um conjunto de números reais, armazenando-0 em vetor e calcular o quadrado das componentes deste vetor, 
armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v2 = []

for x in v1:
    quadrado = x ** 2
    v2.append(quadrado)

print(v1)
print(v2)
