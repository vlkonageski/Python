"""
Faça um programa que leia um numero inteiro positivo impar N e imprima todos os numeros impares de 1 ate N em ordem crescente.
"""

num = 0
numero = int(input('Informe um numero inteiro positivo impar: '))

while numero != num:
    num = num + 1
    if num % 2 != 0:
        print(num)
