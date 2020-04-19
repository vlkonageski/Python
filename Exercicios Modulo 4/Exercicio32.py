"""
Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""

n = int(input("Informe um numero:"))
sucessor = (n * 3) + 1
antecessor = (n * 2) - 1

soma = sucessor + antecessor

print("Numero:", n)
print("Sucessor do triplo é:", sucessor)
print("Antecessor do dobro é:", antecessor)
print("A soma do sucessor do triplo com o dobro é:", soma)
