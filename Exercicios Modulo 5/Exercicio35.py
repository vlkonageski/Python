"""
Leia uma data e determine se ela é valida. Ou seja, verifique se o mes esta entre 1 e 12, e se o dia
existe naquele mes. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos nao bissextos.
"""

dia = int(input("Informe o dia:"))
mes = int(input("Informe o mes:"))
ano = int(input("Informe o Ano:"))


def data():
    if mes >= 1 and mes <= 12:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 0 and dia <= 31:
                print(f"Data valida {dia}/{mes}/{ano}")
            else:
                print("Data Invalida!")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 0 and dia <= 30:
                print(f"Data valida {dia}/{mes}/{ano}")
            else:
                print("Data Invalida!")
        elif mes == 2:
            if ano % 400 == 0:
                if dia > 0 <= 29:
                     print(f"Data valida {dia}/{mes}/{ano}")
                else:
                    print("Data Invalida!")
            elif ano % 4 == 0 and ano % 100 != 0:
                if dia > 0 <= 29:
                     print(f"Data valida {dia}/{mes}/{ano}")
                else:
                    print("Data Invalida!")
            else:
                if dia > 0 <= 28:
                     print(f"Data valida {dia}/{mes}/{ano}")
                else:
                    print("Data Invalida!")


data()
