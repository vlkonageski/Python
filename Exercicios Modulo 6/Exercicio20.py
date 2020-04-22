"""
Ler uma sequencia de numeros inteiros e determinar se eles sao pares ou nao. Deverá ser informado o numero de dados lidos
e numero de valores pares. O processo termina quando for digitado o numero 1000.
"""

par = num = numero = 0

while numero != 1000:
    numero = int(input('Informe um numero: '))
    num = num + 1
    if numero % 2 == 0:
        par = par + 1
if numero == 1000:
    print('1000 digitado, Fim do programa!')
print('Foram digitados {} numeros'.format(num))
print('{} deles sao pares'.format(par))
