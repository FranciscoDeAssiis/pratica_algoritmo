# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
# 450 + 400 + 350 + 300 + ... + 50 + 0

i = 500
s = 0
while i >= 0:
    s += i
    if not i == 0:
        print(i, end=' + ')
    else:
        print(i)
    i -= 50
    # print(s)

print(f'Soma: {s}')
