"""
Faça um programa que calcule e escreva o valor de S
            1 + 3 + 5 + 7     99
        S= --  --  --  -- ... --
            1   2   3   4     50
"""

s1 = 0
s2 = 0

for i in range(1, 50):
    if i % 2 != 0:
        s1 += 1
        s2 += i
resultado = s2 / s1

print(s2)
print(s1)
print(resultado)
