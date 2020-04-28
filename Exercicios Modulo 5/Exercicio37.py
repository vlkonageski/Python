"""
Leia uma data de nascimento de uma pessoa fornecida atraves de tres numeros inteiro:
Dia, Mes e Ano. Teste a validade desta data para saber se esta é uma data valida. Teste
se o dia fornecido é um dia valido: dia > 0, dia <= 28 para o mes de fevereiro (29 se o ano for bissexto)
dia <=30 em abril, junho, setembro e novembro, dia <=31 nos outros meses. Teste a validade do mes: mes >0 e 
mes <13.Teste a validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008). 
Imprimir. "data valida" ou "data invalida" no final da execução do programa.
"""
dia = int(input("Informe o dia de nascimento:"))
mes = int(input("Informe o mes de nascimento:"))
ano = int(input("Informe o ano de nascimento:"))

if ano % 400 == 0 and mes == 2 and dia > 0 and dia <= 29:
    print(f"Data valida {dia}/{mes}/{ano}")
elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 and dia > 0 and dia <= 29:
    print(f"Data valida {dia}/{mes}/{ano}")
elif mes == 2 and dia > 0 and dia <= 28:
    print(f"Data valida {dia}/{mes}/{ano}")
elif mes == mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia > 0 and dia <= 31:
    print(f"Data valida {dia}/{mes}/{ano}")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 0 and dia <= 30:
    print(f"Data valida {dia}/{mes}/{ano}")
else:
    print("Data Invalida")
