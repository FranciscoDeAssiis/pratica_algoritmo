# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Faça um algoritmo que mostre na tela a seguinte contagem:
# 10 9 8 7 6 5 4 3 Acabou!

for x in (range(10, 2, -1)):
    print(x, end=' ')
print('Acabou!')

i = 10
while i >= 3:
    print(i, end=' ')
    i -= 1
print('Acabou!')
