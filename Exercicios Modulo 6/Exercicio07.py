"""
Faça um programa que leia 10 inteiros positivos, ignorando nao positivos, e imprima sua media.
"""

x = 0
soma = 0

while x < 10:
    n = int(input("Informe um numero:"))
    if n > 0:
        x += 1
        soma += n
    else:
        x += 0
        soma = soma
        print("Informe um numero positivo!")

media = soma / x
print("A soma dos numeros é:", soma)
print(f"A media dos numeros é:{media}")
