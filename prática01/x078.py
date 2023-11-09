# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Escreva um programa que leia 15 números e guarde-os em um vetor. No final,
# mostre o vetor inteiro na tela e em seguida mostre em que posições foram
# digitados valores que são múltiplos de 10.

from random import randrange

vetor = [randrange(10, 100) for x in range(15)]
# for x in range(1, 16):
#     vetor.append(int(input(f'{x}º Número: ')))

print(len(vetor), vetor)

for n, x in enumerate(vetor):
    if n < 15:
        if x % 10 == 0:
            print(f'\33[34m[{x}]\33[m', end=', ')
    else:
        print(f'[{x}]')
print()
for x in vetor:
    if x % 10 == 0:
        print(f'\33[36mÍndice {vetor.index(x)}\33[m: {x} é múltiplo de 10.')

