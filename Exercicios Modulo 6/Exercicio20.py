"""
Ler uma sequencia de numeros inteiros e determinar se eles sao pares ou nao. Deverá ser informado o numero de dados lidos
e numero de valores pares. O processo termina quando for digitado o numero 1000.
"""

n = 0
dados_lidos = 0
numeros_par = 0

while n != 1000:
    n = int(input('Informe um numero inteiro:'))
    dados_lidos += 1
    if n % 2 == 0:
        numeros_par += 1
    
print('Foram digitados {} numeros'. format(dados_lidos))
print('Foram digitados {} numeros pares'.format(numeros_par))
