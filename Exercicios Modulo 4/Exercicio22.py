"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros.
A formula de conversao é: M = 0.91 * J, sendo o J o comprimento em jardas e M o comprimento em metros.
"""

j = float(input("Informe o comprimento em Jardas:"))
m = 0.91 * j

print("Jardas:{:.2f}".format(j))
print("Metros:{:.2f}".format(m))
