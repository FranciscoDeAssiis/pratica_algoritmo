# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa que leia 6 números inteiros e no final mostre quantos deles
# são pares e quantos são ímpares.

i = impar = par = 0

while i < 6:
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 == 0:
        if not num == 0:
            par += 1
    else:
        impar += 1
    i += 1

print(f'Pares: {par}\nImpares: {impar}')
