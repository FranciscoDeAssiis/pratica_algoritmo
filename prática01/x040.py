# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Crie um aplicativo que mostre na tela a seguinte contagem:
# 0 3 6 9 12 15 18 Acabou!

for x in range(0, 19, 3):
    print(x, end=' ')
print('Acabou!')

i = 0
while i <= 18:
    print(i, end=' ')
    i += 3
print('Acabou!')
