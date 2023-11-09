# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Escreva um programa que leia um número qualquer e mostre a tabuada desse
# número, usando a estrutura “para”.
# Ex: Digite um valor: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 ...

fator = int(input('Tabuada de qual número: '))
for x in range(1, 11):
    print(f'{fator} x {x} = {fator * x}')
