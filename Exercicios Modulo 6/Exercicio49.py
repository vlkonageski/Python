"""
O  funcionario Carlos tem um colega chamado João que recebe um salario que equivale a um terço do seu salario.
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salario integralmente nela, pois esta
rendendo 2% ao mes. João aplicara seu salario integralmente no fundo de renda fixa, que está rendendo 5% ao mes.
Construa um programa que deverá calcular e mostrar a quantidade de meses necessarios para que o valor pertencente a João
iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.
"""
meses = 0
salario_carlos = 1500
salario_joao = salario_carlos / 2

aplicacao_carlos = salario_carlos * 0.02
aplicacao_joao = salario_joao * 0.05

rendimento_carlos = salario_carlos + aplicacao_carlos
rendimento_joao = salario_joao + aplicacao_joao

saldo_carlos = rendimento_carlos + aplicacao_carlos
saldo_joao = rendimento_joao + aplicacao_joao

while saldo_joao <= saldo_carlos:
    saldo_carlos += aplicacao_carlos
    saldo_joao += aplicacao_joao
    meses += 1

print('Rendimento aplicacao Joao', saldo_joao)
print('Rendimento aplicacao Carlos', saldo_carlos)
print('Quantidade de meses para o rendimento de Joao ultrapassar o de Carlos', meses)
