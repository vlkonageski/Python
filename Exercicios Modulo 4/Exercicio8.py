"""
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
A formula de conversao é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

k = float(input("Informe a temperatura em Graus Kelvin:"))
c = k - 273.15

print("Kelvin:{:.2f}".format(k))
print("Celsius:{:.2f}".format(c))
