"""
Dados N e dois numeros inteiros positivos, I e J, diferentes de 0, imprimir em ordem crescente os N primeiros 
naturais que são multiplos de I ou de J e ou de ambos. Exemplo: Para N = 6, I = 2 e J = 3 a saída devera ser:
0,2,3,4,6,8.
"""

n = int(input('Informe um numero:'))
i = 2
j = 3
x = 0
y = 0 

while x != n:
    if y % i == 0:
        print(y)
        y += 1
        x += 1
    elif y % j == 0:
        print(y)
        y += 1
        x += 1
    elif y % i == 0 and y % j == 0:
        print(y)
        y += 1
        x += 1
    else:
        y += 1
