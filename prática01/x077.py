# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No
# final, mostre uma listagem com todos os nomes informados, na ordem inversa
# daquela em que eles foram informados.

vetor = []

for i in range(7):
    vetor.append(str(input(f'{i}ª Nome: ')))
vetor.reverse()
print(vetor)
