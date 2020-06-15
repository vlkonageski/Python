"""
Faça um programa que calcule o termo pitagorico A, B, C = 1000. Um terno pitagorico é um conjunto de tres
numeros naturais, A, B, C, para a qual,
                                A² + B² = C²
Por exemplo,
                                3² + 4² = 9 + 16 = 25 = 5²
"""

a = int(input('Informe o valor de A:'))
b = int(input('Informe o valor de B:'))
c = int(input('Informe o valor de C:'))

quadrado_a = a ** 2
quadrado_b = b ** 2
quadrado_c = c ** 2
soma = quadrado_a + quadrado_b

if soma == quadrado_c:
    print('É um termo Pitagorico!')
    print('{}² + {}² = {} + {} = {} = {}²'.format(a, b, quadrado_a, quadrado_b, soma, c))

else:
    print('Não é um termo Pitagorico!')


