"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
A formula de conversão é: F = C * (9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""

c = float(input("Informe a temperatura em graus Celsius:"))
f = c * (9 / 5) + 32

print("Celsius:{:.2f}".format(c))
print("Fahrenheit:{:.2f}".format(f))
