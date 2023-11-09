# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
# No final, mostre quais são os números pares que foram digitados e em que
# posições eles estão armazenados.

vetor = [int(input(f'{x+1}º Número: ')) for x in range(10)]

for i, x in enumerate(vetor):
    if x % 2 == 0 and x != 0:
        if x == vetor[0]:
            print('Números pares: ')
        else:
            print(f'índice: {i}, valor: {x}')

