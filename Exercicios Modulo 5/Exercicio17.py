"""
Faça um programa que calcule e mostre a area de um trapezio. Sabe-se que:
            A = (basemaior + basemenor) * altura
            ------------------------------------
                            2
Lembre-se a base maior e a base menor devem ser numeros maiores que zero.
"""

basemaior = float(input("Informe o valor da Base maior:"))
basemenor = float(input("Informe o valor da Base menor:"))
altura = float(input("Informe a altura:"))

if basemaior > 0 and basemenor > 0:
    a = ((basemaior + basemenor) * altura) / 2
    print("A area do trapezio é:", a)
else:
    print("A base maior e a base menor devem ser maior que zero!")
