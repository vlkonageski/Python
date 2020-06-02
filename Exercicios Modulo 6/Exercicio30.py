"""
Faça programas para calcular as seguintes sequencias:
            1 + 2 + 3 + 4 + 5 + ... + N
            1 - 2 + 3 - 4 + 5 ... + (2N - 1)
            1 + 3 + 5 + 7 + ... + (2N - 1)
"""

n = int(input('Informe um numero:'))
c1 = 0
c2 = 0
c3 = 0

for i in range (1, n+1):
    c1 += i
    if i % 2 == 0:
        c2 += i
    else:
        c2 -= i
        c3 += i
print(c1)
print(c2)
print(c3)