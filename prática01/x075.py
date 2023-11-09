# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Crie um programa que preencha automaticamente (usando lógica, não apenas
# atribuindo diretamente) um vetor numérico com 15 posições com os primeiros
# elementos da sequência de Fibonacci:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
# 0 1 2 3 4 5 6  7  8  9  10 11  12  13  14  15

vetor = []

a1 = 0
b1 = 1
c1 = 0
vetor.append(0)
for _ in range(15+1):
    c1 = a1 + b1
    a1 = b1
    b1 = c1
    vetor.append(a1)
print(vetor)
