"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequencia arbitraria de
notas (validas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente media aritmetica.
O numero de notas com que o aluno pretenda efetuar o calculo nao sera fornecido ao programa, o qual terminara quando for
introduzido um valor que nao seja valido como nota de aprovação.
"""

numero = 10
media = 0
nota = 0

while numero >= 10 and numero <= 20:
    num = int(input('Informe uma nota entre 10 e 20: '))
    if num >= 10 and num <= 20:
        media = media + 1
        if num >= 10 and num <= 20:
            nota = num
            nota += nota
            calculo = nota / media
    else:
        break
        print('Programa encerrado')
print(media)
print(calculo)
