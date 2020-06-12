"""
Faça um programa que some os numeros impares contidos em um intervalo definido pelo usuario. O usuario define
o valor inicial do intevalo e o valor final deste intervalo e o prorama deve somar todos os numeros impares 
contidos neste intervalo. Caso o usuario digite um intervalo invalido (começando por um valor maior que o valor
final) deve ser escrito uma mensagem de erro na tela, "Intervalo de valores invalido" e o programa termina. 
Exemplo de tela de saida:
DIGITE O VALOR INICIAL E VALOR FINAL: 5 10
SOMA DOS IMPARES NESTE INTERVALO: 21
"""

x= int(input('Digite o valor inicial do intervalo:'))
y= int(input('Digite o valor final do intervalo:'))
soma = 0
if x <= y:
    for n in range(x, y+1):
        if n % 2 != 0:
            soma += n 
    print('A soma dos impares do intervalo entre {} e {} = {}'.format(x, y, soma)) 
else:
    print('Intervalo de valores invalido')
        
   
