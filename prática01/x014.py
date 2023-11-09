# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
# um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

km = float(input('Total de quilômetros percorridos(Km): '))
dias_alugado = int(input('Total de dias alugado: '))

PREÇO_POR_KM = 0.2
PREÇO_POR_DIA = 90

preço_total = km * PREÇO_POR_KM + dias_alugado * PREÇO_POR_DIA

print(f'Total a pagar: R$:{preço_total:,.2f}')
