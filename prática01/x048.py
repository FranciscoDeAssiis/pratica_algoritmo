# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Faça um programa que leia 7 números inteiros e no final mostre o somatório
# entre eles.

som = 0
for x in range(1, 7+1):
    num = int(input(f'Digite {x}º número: '))
    som += num

print(f'Soma total: {som}')


i = s = 0
while i < 7:
    n = int(input(f'Digte {i+1}º número: '))
    s += n
    i += 1
print(f'Soma total: {s}')

