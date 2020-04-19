"""
Sejam a e b os catetos de um triangulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz quadrada de a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa atraves da equação. Imprima o resultado dessa opreção.
"""
import math

a = float(input("Informe o valor de A:"))
b = float(input("Informe o valor de B:"))
soma = (a * a) + (b * b)

hipotenusa = float(math.sqrt(soma))

print("O resultado da operacao é:{:.2f}".format(hipotenusa))
