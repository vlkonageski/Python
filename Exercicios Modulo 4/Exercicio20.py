"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras.
A formula de conversao é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

k = float(input("Informe a massa em quilogramas:"))
l = k / 0.45

print("Quilogramas:{:.2f}".format(k))
print("Libras:{:.2f}".format(l))
