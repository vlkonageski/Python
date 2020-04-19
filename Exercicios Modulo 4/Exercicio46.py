"""
Faca um programa que leia um numero inteiro positivo de tres digitos( de 100 a 999).
Gere outro numero formado pelos digitos invertidos do numero lido. Exemplo:
    NumeroLido = 123
    NumeroGerado = 321.
"""

numero = str(input("Informe um numero de 3 digitos de 100 a 999:"))

reverso = numero[::-1]

print("Inverso do numero:", reverso)
