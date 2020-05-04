"""
Escreva um algoritmo que leia certa quantidade de numeros e imprima o maior deles e quantas vezes o maior
numero foi lido. A quantidade de numeros a serem lidos deve ser fornecida pelo usuario.
"""

n = int(input("Informe a quantidade de numeros a serem forncecidos:"))
x = 0
cont = 0
lista = []

while x != n:
    numero = int(input("Informe um numero:"))
    lista.append(numero)
    maior = max(lista)
    if numero in lista == maior:
        cont += 1
    else:
        cont == cont 
    x += 1   

print(cont)
print(maior)
