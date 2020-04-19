"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A formula de conversao é: C = P * 2.54, sendo C o comprimento em centimetros e P o comprimento em polegadas.
"""

p = float(input("Informe o comprimento em Polegadas:"))
c = p * 2.54

print("Polegadas:{:.2f}".format(p))
print("Centimetros:{:.2f}".format(c))
