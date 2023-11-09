# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

#  Crie um programa que leia o número de dias trabalhados em um mês e mostre o
# salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
# por hora trabalhada.

dias_tabalhados = int(input('Total de dias trabalhados no mês: '))

SALARIO_POR_HORA = 25
HORAS_POR_DIA = 8

salario_diario = HORAS_POR_DIA * SALARIO_POR_HORA
salario_mensal = dias_tabalhados * salario_diario

print(f'Salário de R${salario_mensal} por {dias_tabalhados} dias trabalhados.')
