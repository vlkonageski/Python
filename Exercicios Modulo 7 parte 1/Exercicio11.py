"""
Faça um programa que preencha um vetor com 10 numeros reais, calcule e mostre a quantidade de numeros negativos e a soma
dos numeros positivos desse vetor.
"""

v = []
n = 0
negativo = 0
positivo = 0

while n < 10:
    n = n + 1
    numero = int(input("Informe um numero real: "))
    v.append(numero)

    if numero < 0:
        negativo = negativo + 1
    else:
        positivo = positivo + numero

print(v)
print(f'O vetor possui {negativo} números negativos')
print(f'A soma dos numeros positivos do vetor é = {positivo}')
