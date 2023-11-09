# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Faça um programa usando a estrutura “para” que leia um número inteiro
# positivo e mostre na tela uma contagem de 0 até o valor digitado:
# Ex: Digite um valor: 9
# Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!

fin = int(input('Contar até: '))
for x in range(0, fin+1):
    print(x, end=', ')
print('FIM!')
