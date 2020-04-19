"""
Leia um valor de volume em litros e apresente-o convertido em metros cubicos m³.
A fórmula de conversão é: M = L / 1000 , sendo L o volume em litros e M o volume em metros cubicos.
"""

l = float(input("Informe o volume em Litros:"))
m = l / 1000

print("Litros:{:.2f}".format(l))
print("Metros Cubicos:{:.2f}".format(m))
