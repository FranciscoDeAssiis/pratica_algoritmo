# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Crie um programa que preencha automaticamente um vetor numérico com 7
# números gerados aleatoriamente pelo computador e depois mostre os valores
# gerados na tela.
from random import randrange
vetor = []
for _ in range(7+1):
    vetor.append(randrange(start=1, stop=100))
print(vetor)
