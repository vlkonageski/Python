"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""
v = []
x = 0

while x < 5:
    n = int(input('Informe um numero:'))
    x += 1
    v.append(n)

print(v)
print('O maior elemento da lista se encontra na posição:', v.index(max(v)))
print('O maior elemento da lista se encontra na posição:', v.index(min(v)))
