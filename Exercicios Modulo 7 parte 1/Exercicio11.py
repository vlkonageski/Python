"""
Faça um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos
e a soma dos numeros positivos desse vetor.
"""

v = []
x = 0
negativos = 0
soma = 0

while x < 10:
    n = int(input('Informe um numero real:'))
    x += 1
    v.append(n)
    if n < 0:
        negativos += 1
    else:
        soma += n

print(v)
print('Existem {} numeros neagtivos no vetor.'.format(negativos))
print('A soma dos numeros positivos do vetor é:{}'.format(soma))
