"""
Crie um program que le 6 valores inteiros e, em seguida, mostre na tela os valores lidos.
"""
# Inicia a contagem de vezes em 0
n = 0
#Cria uma lista vazia
v = []
#Laço de repetição para repetir o processo 6 vezes
while n < 6:
#Cada vez que repetir o processo soma-se 1 em n
    n = n + 1
#Solicita o numero ao usuario
    numero = int(input("Informe um numero:"))
#Adiciona os numeros informados pelo usuario a lista
    v.append(numero)
#Imprime a lista
print(v)
