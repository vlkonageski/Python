"""
Faça um program que possua um vetor denominado A que armazene 6 numeros inteiros. O programa deve executar
os seguintes passos:
(a)Atribua os seguintes valores a esse vetor: 1,0,5,-2,-5,7.
(b)Armazene em uma variavel interia (simples) a soma entre os valores das posições A[0],A[1] e A[5] do vetor
e mostre na tela a soma.
(c)Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
(d)Mostre na tela cada valor do vetor A, um em cada linha.
"""

# criando o vetor A
a = [1, 0, 5, -2, -5, 7]

# Soma entre os valores das posições A[0],A[1] e A[5] 
soma = a[0] + a[1] + a[5]
print('A soma entre os valores das posições A[0],A[1] e A[5] =', soma)

#Modificando o vetor na posição 4, atribuindo a esta posição o valor 100.
a.insert(4, 100)

#Imprimindo cada valor do vetor A, um em cada linha.

for x in a:
    print(x)
