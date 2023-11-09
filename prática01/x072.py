# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 5 10 15 20 25 30 35 40 45 50
# 0 1  2  3  4  5  6  7  8  9

velor = []
for x in range(50 + 1):
    if x % 5 == 0:
        velor.append(x)

print(velor)  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
