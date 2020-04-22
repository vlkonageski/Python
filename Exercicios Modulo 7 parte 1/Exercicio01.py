"""
Faça um program que possua um vetor denominado A que armazene 6 numeros inteiros. O programa deve executar os seguintes passos:
(a)Atribua os seguintes valores a esse vetor: 1,0,5,-2,-5,7.
(b)Armazene em uma variavel interia (simples) a soma entre os valores das posições A[0],A[1] e A[5] do vetor e mostre na tela a soma.
(c)Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d)Mostre na tela cada valor do vetor A, um em cada linha.
"""

#Atribuindo valores ao vetor
A = [1,0,5,-2,-5,7]

#Somando e imprimindo os valores do vetor
soma = A[0] + A[1] + A[5]
print(f'A soma dos valores das posições A[0], A[1] e A[5] é = {soma}')

#Alterando o valor da posição [4] do vetor
A[4] = 100

#Imprimindo os valores do vetor um em cada linha
for numero in A:
    print(numero)
