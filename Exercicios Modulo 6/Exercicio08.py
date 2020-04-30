"""
Escreva um programa que leia 10 numeros e escreva o menor valor lido e o maior valor lido.
"""

x = 0
lista = []

while x < 10:
    x += 1
    n = int(input("Informe um numero:"))
    lista.append(n)

print("O maior numero digitado foi:", max(lista))
print("O menor numero digitado foi:", min(lista))
