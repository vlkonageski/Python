"""
Faça um programa que receba dois numeros. Calcule e mostre:
º a soma dos numeros pares desse intervalo de numeros. incluindo os numeros digitados;
º a multiplicação dos numeros impares desse intervalo, incluindo os digitados;
"""

n1 = int(input('Informe um numero inteiro:'))
n2 = int(input('Informe um numero inteiro:'))
soma = 0
multiplicacao = 1

while n1 != n2:
    n1 += 1
    if n1 % 2 == 0:
        soma += n1 
    else:
        multiplicacao *= n1 

print('A soma dos numeros pares do intervalo e:', soma)
print('A multiplicacao dos numeros impares do intervalo e:', multiplicacao)
