"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A formula de conversão é: H = M * 0.0001, sendo M a area em metros quadrados e H a área em hectare.
"""

m = float(input("Informe a area em metros quadrados:"))
h = m * 0.0001

print("Metros Quadrados:{:.2f}".format(m))
print("Hectares:{:.2f}".format(h))
