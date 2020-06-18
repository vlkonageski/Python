"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior,
o menor e a media dos valores.
"""

v = []
x = 0
soma = 0

while x < 5:
    n = int(input('Informe um numero:'))
    x += 1
    v.append(n)
    soma += n

media = soma / x

print(v)
print('O maior valor lido é:', max(v))
print('O menor valor lido é:', min(v))
print('A media dos valores lidos é:', media)
