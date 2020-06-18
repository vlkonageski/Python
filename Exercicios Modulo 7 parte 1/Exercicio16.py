"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o codigo for zero, finalize o programa; se o codigo for 1, mostre o vetor na ordem direta; 
se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 1 e 2 escreva uma mensagem
 informando que o código é inválido.
"""

v = []
x = 0

while x < 5:
    n = int(input('Informe um numero real:'))
    x += 1
    v.append(n)

opcao = int(input('     MENU DE OPÇÕES\n'
                '1 - Vetor na ordem direta\n'
                '2 - Vetor na ordem inversa\n'
                'Informe a opção desejada:'))

if opcao == 1:
    print(v)
elif opcao == 2:
    v.reverse()
    print(v)
else:
    print('Opção Invalida!')
