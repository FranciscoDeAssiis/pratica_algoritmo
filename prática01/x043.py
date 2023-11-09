# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1,
# marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
# 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...

for x in range(30, -1, -1):
    if x % 4 == 0:
        print(f'\33[1;32m[{x}]\33[m', end=' ')
    else:
        print(x, end=' ')

print()

i = 30
while i >= 0:
    if i % 4 == 0:
        print(f'\33[1;32m[{i}]\33[m', end=' ')
    else:
        print(i, end=' ')
    i -= 1
