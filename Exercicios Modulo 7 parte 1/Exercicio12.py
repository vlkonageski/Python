"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a
media dos valores.
"""

v = []
n = 0

while n < 5:
    n = n + 1
    numero = int(input('Informe um valor: '))
    v.append(numero)

print(v)
print(f'Maior {max(v)}')
print(f'Menor {min(v)}')
print(f'Media {sum(v) / len(v)}')
