# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# ) Crie um programa que mostre na tela a seguinte contagem, usando a estrutura
# “faça enquanto”
# 0 3 6 9 12 15 18 21 24 27 30 Acabou!

i = 0
while i <= 30:
    if i != 30:
        print(i, end=' ')
    else:
        print(i, end=' Acabou!')
    i += 3
