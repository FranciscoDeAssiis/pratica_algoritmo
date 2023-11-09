# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
# mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3

from random import randint

numbers = [randint(0, 10) for x in range(0, 20)]
acima = [x for x in numbers if x > 5]
div_3 = [x for x in numbers if x % 3 == 0 and not x == 0]
print(f'\33[1;32mNúmeros sorteados\33[33m: {numbers}')

print()

print(f'\33[1;32mNúmeros acima de 5\33[m: \33[1;34m{len(acima)}\33[m - {acima}') # Média entre 8 e 13 números acima de 5
print(f'\33[1;32mNúmeros divisíveis por 3\33[m : \33[1;34m{len(div_3)}\33[m  - {div_3}')

print()

print('Acima de 5:      ', end='')
for x in numbers:
    if x in acima:
        print(f'\33[1;34m[{x}]\33[m', end=' ')
    else:
        print(f'\33[30m[{x}]\33[m', end=' ')

print()

print('Divisível por 3: ', end='')
for x in numbers:
    if x in div_3:
        print(f'\33[35m[{x}]\33[m', end=' ')
    else:
        print(f'\33[30m[{x}]\33[m', end=' ')

print()

