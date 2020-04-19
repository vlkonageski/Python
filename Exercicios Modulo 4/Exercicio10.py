# -*- coding: utf-8 -*-
"""
Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo).
A formula de conversao é: M = K/3.6, sendo K a velocidade em Km/h e M em m/s.
"""

k = float(input("Informe a velocidade em Km/h:"))
m = k / 3.6

print("Km/h:{:.2f}".format(k))
print("m/s:{:.2f}".format(m))
