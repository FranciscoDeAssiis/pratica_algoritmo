# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
# seu novo salário, com 15% de aumento.

salário = float(input('Salário(R$): '))

DESCONTO = 15

novo_salário = salário + (DESCONTO * salário / 100)

print(f'Novo salário com {DESCONTO}% de desconto: R$:{novo_salário:,.2f}')

