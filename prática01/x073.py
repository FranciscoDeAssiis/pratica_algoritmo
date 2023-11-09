# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
# 9 8 7 6 5 4 3 2 1 0
# 0 1 2 3 4 5 6 7 8 9
vetor = [[x for x in range(9, -1, -1)]]

i = 12
v = []
while i > -1:
    v.append(i)
    i -= 1

print(vetor)
print(v)
