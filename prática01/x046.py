# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa que calcule e mostre na tela o resultado da soma entre 6 +
# 8 + 10 + 12 + 14 + ... + 98 + 100.


soma = 0
i = 6
while i < 100+1:
    soma += i
    if i < 100:
        print(f'{i}', end=' + ')
    else:
        print(f'{i}.')
    i += 2
    # print(soma)

print(f'Soma: {soma}')
