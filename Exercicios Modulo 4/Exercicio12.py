"""
Leia uma distancia em milhas e apresente-a convertida em quilometros.
A formula de conversao é: K = 1.61 * M, sendo K a distancia em quilometros e M em milhas.
"""

m = float(input("Informe a velocidade em milhas:"))
k = 1.61 * m

print("Milhas:{:.2f}".format(m))
print("Km/h:{:.2f}".format(k))
