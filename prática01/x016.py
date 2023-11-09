# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

#  [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
# fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
# já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
# quantos dias de vida um fumante perderá e exiba o total em dias.

cigarros_por_dia = int(input('Total de cigarros fumados por dia: '))
total_de_anos = int(input('Fumante por quantos anos: '))

MIN = 10  # 1 cigarro custa 10 minutos de vída.

total_de_dias = total_de_anos * 365  # transformando anos em dias
total_de_cigarros = cigarros_por_dia * total_de_dias  # cigarros do dia vezes todos os dias
total_de_minutos = total_de_cigarros * MIN  # todos os cigarros multiplicados por 10 minutos
total_de_dias = total_de_minutos / 1440  # 1440 é igual 1 dia
total_de_anos = total_de_dias / 365  # 365 é igual a 1 ano

print(f'Perderá {total_de_dias:.0f} dias de vida.')
