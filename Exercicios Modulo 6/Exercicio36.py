"""
Faça um programa que calcule a diferença  ente a soma dos quadrados dos primeiros 100 numeros naturais e o 
quadrado da soma.
EX: A soma dos quadrados dos dez primeiros numeros naturais é,
            1² + 2² + ... + 10² = 385
O quadrado da soma dos dez primeiros numeros naturais é,
            (1 + 2 + ... + 10)² = 552 = 3025
A diferença entre a soma dos quadrados dos dez primeiros numeros naturais e o quadrado da soma é 3025-385 = 2640
"""
soma_quadrados = 0
soma = 0
for x in range(1, 101):
    quadrado = x ** 2
    soma_quadrados += quadrado

for y in range(1, 101):
    soma += y
    quadrado_soma = soma ** 2

diferenca = quadrado_soma - soma_quadrados

print(soma_quadrados)
print(quadrado_soma)
print('A diferença entre a soma dos quadrados dos cem primeiros numeros naturais e'
' o quadrado da soma é {} - {} = {}'.format(quadrado_soma, soma_quadrados, diferenca))
