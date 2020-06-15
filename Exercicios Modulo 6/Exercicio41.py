"""
Faça um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos pelo usuario via 
teclado. O programa fica pedindo estes valores e calculando ate que o usuario entre com um valor para 
resistencia igual a zero.
                        R1 * R2
                     R=---------
                        R1 + R2
"""

while True:
   r1 = int(input('Informe o valor de R1:'))
   r2 = int(input('Informe o valor de R2:'))
   if r1 > 0 and r2 > 0:
      r = (r1 * r2) / (r1 + r2)
      print('R = ', r)
   else:
      print('Programa Finalizado!')
      break
