"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
"""

v = [1, 2, 3, 4, 5, 6, 7, 2, 3, 10]
v2 = []
for x in v:
    if v.count(x) > 1:
        v2.append(x)

print(v2)
