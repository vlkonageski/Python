"""
Faça um programa que leia um numero indeterminado de idades de individuos (pare quando for informada a idade 0),
e calcule a idade media desse grupo.
"""
x = 0
soma_idade = 0
while True:
    idade = int(input('Informe a idade do individuo:'))
    if idade > 0:
        x += 1
        soma_idade += idade
    else:
        print('Programa Finalizado!')
        break

print('A media de idades é: {:.2f}'.format(soma_idade / x))
