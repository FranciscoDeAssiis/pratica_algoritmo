# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Desenvolva um programa que mostre na tela a seguinte contagem:
# 100 95 90 85 80 ... 0 Acabou

for x in range(100, -1, -5):
    print(x, end=' ')
print('Acabou!')

i = 100
while i >= 0:
    print(i, end=' ')
    i -= 5
print('Acabou!')
