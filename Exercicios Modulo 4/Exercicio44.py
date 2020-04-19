"""
Receba a altura do degrau de uma escada e a altura que o usuario deseja alcancar subindo a escada.
Calcule e mostre quantos degraus o usuario devera subir para atingir seu objetivo.
"""

degrau = int(input("Informe a altura do degrau em centimetros:"))
altura = int(input("Informe a altura que deseja subir em centimetros"))

qtd_degruas = altura / degrau

print("A quantidade de degraus a subir é de:", qtd_degruas)
