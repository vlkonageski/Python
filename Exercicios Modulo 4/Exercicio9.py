"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A formula de conversao é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""

c = float(input("Informe a temperatura em graus Celsius: "))
k = c + 273.15

print("Celsius:{:.2f}".format(c))
print("Kelvin:{:.2f}".format(k))
