# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
# na tela uma das mensagens abaixo:
#  - O primeiro valor é o maior
#  - O segundo valor é o maior
#  - Não existe valor maior, os dois são iguais

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, ambos são iguais!')
