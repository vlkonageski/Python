"""
Escreve um programa que verifique quais numeros entre 1000 e 9999 (inclusive) possuem a propriedade seguinte:
a soma dos dois digitos de mais baixa ordem com os dois digitos de mais alta ordem elevada ao quadrado e igual
ao proprio numero. Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""

for n in range(1000, 9999):
    milhar = int((n % 10000) / 100)
    dezenas = n % 100
    soma = milhar + dezenas
    elevado = soma ** 2
    if elevado == n:
        print(n)
        print('{} + {} = {}'.format(milhar, dezenas, soma))
        print('{}² = {}'.format(soma, elevado))
        print()

