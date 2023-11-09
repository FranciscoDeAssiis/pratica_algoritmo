# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

#  O programa acima vai ter um problema quando digitarmos o primeiro valor
# maior que o último. Resolva esse problema com um código que funcione em qualquer
# situação.

ini = int(input('Valor inicial: '))
fin = int(input('Valor final: '))

if ini > fin:
    salto = -2
else:
    salto = 2

for x in range(ini, fin+1, salto):
    print(x, end=' ')
    if x == fin - 1:
        print('Acabou!')


if ini < fin:
    print('\nEntrou no inicio menor')
    i = ini
    while i <= fin:
        print(i, end=' ')
        if i == fin - 1:
            print('Acabou!')
        i += 2
else:
    print('\nEntrou no final maior')
    i = fin
    while i <= ini:
        print(i, end=' ')
        if i == ini - 1:
            print('Acabou!')
        i += 2
