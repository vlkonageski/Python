# Peça ao usuario para digitar três valores inteiros e imprima a soma deles

n = 0
soma = 0
while n < 3:
    n = n + 1
    num = int(input('Informe um numero inteiro: '))
    soma = soma + num

print('A soma dos três valores é:', soma)
