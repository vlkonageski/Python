"""
Leia um valor de comprimento em metros e apresente-o convertido em jardas.
A formula de conversao é: J = M / 0.91, sendo o J o comprimento em jardas e M o comprimento em metros.
"""

m = float(input("Informe o comprimento em Metros:"))
j = m / 0.91

print("Metros:{:.2f}".format(m))
print("Jardas:{:.2f}".format(j))
