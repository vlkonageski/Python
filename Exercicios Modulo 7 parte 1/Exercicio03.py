"""
Ler um conjunto de números reais, armazenando-0 em vetor e calcular o quadrado das componentes deste vetor, armazenando
o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""
#Inicia os vetores vazios e as variaveis iniciadas em 0
v1 = []
v2 = []
n = 0
num = 0

#Faz o loopin para repetir 10 vezes o processo
while n < 10:
    n = n + 1
    numero = int(input("Informe um numero:"))
#Acrescenta os numeros na lista
    v1.append(numero)
#faz um laço de repetição para calcular o quadrado de todos os elementos inseridos na lista
    for num in v1:
       num *= numero
#Acrescenta os numeros ao quadrado a lista
    v2.append(num)

#Imprime as duas listas
print(f'Conjunto simples: {v1}')
print(f'Conjunto de numeros ao quadrado: {v2}')
