"""
Faça uma prova de matematica para crianças que estao aprendendo a somar numeros inteiro menores
do que 100. Escolha numeros aleatorios entre 1 e 100, e mostre na tela a pergunta:
qual é a soma de A + , onde A e B sao os numeros aleatorios. Peça a resposta. 
Faça cinco perguntas ao aluno emostre para ele as perguntas e as respostas corretas,
alem de quantas vezes o aluno acertou.
"""
from random import randint 


def prova():
    perguntas = 0
    acerto = 0
    erro = 0    
    while perguntas < 5:
        perguntas += 1
        n1 = randint(1, 100)
        n2 = randint(1, 100)
        pergunta = float(input(f"Qual a soma de {n1} + {n2}:"))
        soma = n1 + n2
        print("A sua resposta foi:", pergunta)
        print("A resposta correta é:", soma)
        if pergunta == soma:
            acerto += 1
            print("Voce acertou")
        else:
            erro += 1
            print("Voce errou")

    print(f"Voce acertou {acerto} vezes")
    print(f"Voce errou {erro} vezes")


prova()
