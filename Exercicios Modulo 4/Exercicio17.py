"""
Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
A formula de conversao é: P = C / 2.54, sendo C o comprimento em centimetros e P o comprimento em polegadas.
"""

c = float(input("Informe o comprimento em Centimetros:"))
p = c / 2.54

print("Centimetros:{:.2f}".format(c))
print("Polegadas:{:.2f}".format(p))
