"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas.
A formula de conversao é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

l = float(input("Informe a massa em Libras:"))
k = l * 0.45

print("Libras:{:.2f}".format(l))
print("Quilogras:{:.2f}".format(k))
