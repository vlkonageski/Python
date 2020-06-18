"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1), sendo i a posição do
elemento no vetor. Em segida imprima o vetor na tela.
"""

v = []

for i in range(50):
    n = (i + 5 * i) % (i + 1)
    v.append(n)

print(v)
