"""
Leia uma distancia em quilometros e apresente-a convertida em milhas.
A formula de conversao é: M = K / 1.61 , sendo K a distancia em quilometros e M em milhas.
"""

k = float(input("Informe a velocidade em Km/h:"))
m = k / 1.61

print("Km/h:{:.2f}".format(k))
print("Milhas:{:.2f}".format(m))
