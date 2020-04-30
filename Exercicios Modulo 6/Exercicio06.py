"""
Faça um programa que leia 10 inteiros e imprima sua media.
"""

x = 0
soma = 0

while x < 10:
    x += 1
    n = int(input("Informe um numero:"))
    soma += n

media = soma / x
print("A soma dos numeros é:", soma)
print(f"A media dos numeros é:{media}")
