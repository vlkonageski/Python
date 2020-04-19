"""
Leia um angulo em radianos e apresente-o convertido em graus.
A formula de conversao é: G = R * 180 / 3.14, sendo G o angulo em graus e R em radianos e pi = 3.14.
"""

r = float(input("Informe o angulo em Radianos:"))
g = (r * 180) / 3.14

print("Radianos:{:.2f}".format(r))
print("Graus:{:.2f}".format(g))
