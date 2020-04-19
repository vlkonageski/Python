"""
Leia um valor de volume em metros cubicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cubicos.
"""

m = float(input("Informe o volume em Metros Cubicos:"))
l = 1000 * m

print("Metros Cubicos:{:.2f}".format(m))
print("Litros:{:.2f}".format(l))
