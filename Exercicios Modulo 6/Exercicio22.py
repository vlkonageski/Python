"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequencia arbitraria de
notas (validas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente media aritmetica.
O numero de notas com que o aluno pretenda efetuar o calculo nao sera fornecido ao programa, o qual terminara quando for
introduzido um valor que nao seja valido como nota de aprovação.
"""

nota = 10
vezes_digitada = 0
soma = 0

while nota >= 10 and nota <= 20:
    nota = float(input('Informe uma nota entre 10 e 20:'))
    if nota >= 10 and nota <= 20:
        vezes_digitada += 1
        soma += nota

media = soma / vezes_digitada

print('Foram digitadas {} notas'.format(vezes_digitada))
print('A media aritmetica e:', media)
