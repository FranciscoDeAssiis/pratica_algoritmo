# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Faça um algoritmo que pergunte a distância que um passageiro deseja
# percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
# viagens até 200Km e R$0.45 para viagens mais longas.

# 7668 km - de Brasília até Texas (média de 8h 15 min)
# 28574 km - do Brasil até China (média de 35h 03m)
km = float(input('Viagem até o destino. Distância(Km): '))

UP_TO = 0.5
BEYOND = 0.45

if km <= 200:
    preço_passagem = km * UP_TO
else:
    preço_passagem = km * BEYOND

print(f'Total da passagem: R${preço_passagem:,.2f}')
