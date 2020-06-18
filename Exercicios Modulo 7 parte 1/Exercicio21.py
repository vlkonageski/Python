"""
Faça um programa que receba do usuario dois vetores, A e B, com 10 números inteiros cada. Crie um novo
vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C.
"""

a = []
b = []
c = []

for i in range(5):
    n1 = int(input('Informe um numero:'))
    n2 = int(input('Informe um numero:'))
    a.append(n1)
    b.append(n2)

for i in range(5):
    sub = a[i] - b[i]
    c.append(sub)

print(a)
print(b)
print(c)
