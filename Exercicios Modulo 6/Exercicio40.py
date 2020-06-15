"""
Elabore um programa que faça leitura de varios numeros inteiros, ate que se digite um numero negativo.
O programa tem que retornar o maior e o menor numero lido.
"""
n = 0
lista = []
while n >= 0:
    n = int(input('Informe um numero inteiro:'))
    if n >= 0:
        lista.append(n)
    else:
        print('Programa Finalizado!')
        break

print(lista)
print('O maior valor digitado foi:', max(lista))
print('O menor valor digitado foi:', min(lista))
