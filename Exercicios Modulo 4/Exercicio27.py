"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A formula de conversão é: M = H * 10000, sendo M a area em metros quadrados e H a área em hectare.
"""

h = float(input("Informe a area em hectares:"))
m = h * 10000

print("Hectares:{:.2f}".format(h))
print("Metros Quadrados:{:.2f}".format(m))
