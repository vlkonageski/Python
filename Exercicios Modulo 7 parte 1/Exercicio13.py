"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""

v = []
n = 0

while n < 5:
    n = n + 1
    numero = int(input('Informe um valor: '))
    v.append(numero)

print(v)
print(f'O maior valor é {max(v)} e esta na posição {v.index(max(v))} da memoria')
print(f'O menor valor é {min(v)} e esta na posição {v.index(min(v))} da memoria')
