# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
# incremento, mostrando em seguida todos os valores no intervalo:
# Ex:
#   Digite o primeiro Valor: 3
#   Digite o último Valor: 10
#   Digite o incremento: 2
#   Contagem: 3 5 7 9 Acabou!

ini = int(input('Valor inicial: '))
fin = int(input('Valor final: '))

for x in range(ini, fin+1, 2):
    print(x, end=' ')
    if x == fin - 1:
        print('Acabou!')

i = ini
while i <= fin:
    print(i, end=' ')
    if i == fin - 1:
        print('Acabou!')
    i += 2

