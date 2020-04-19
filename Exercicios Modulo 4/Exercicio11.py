"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilometros por hora).
A formula de conversao é: K = M * 3.6, sendo M a velocidade em m/s e K em km/h.
"""

m = float(input("Informe a velocidade em m/s:"))
k = m * 3.6

print("m/s:{:.2f}".format(m))
print("Km/h:{:.2f}".format(k))
