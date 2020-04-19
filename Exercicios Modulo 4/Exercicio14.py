"""
Leia um angulo em graus e apresente-o convertido em radianos.
A formula de conversao é: R = G * 3.14 / 180, sendo G o angulo em graus e R em radianos e pi = 3.14.
"""

g = float(input("Informe o angulo em Graus:"))
r = (g * 3.14) / 180

print("Graus:{:.2f}".format(g))
print("Radianos:{:.2f}".format(r))
