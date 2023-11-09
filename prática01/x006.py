# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
# sucessor.
# Ex:
#   Digite um número: 9
#   O antecessor de 9 é 8
#   O sucessor de 9 é 10


numero = int(input('Digite o número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é {antecessor}\nO sucessor de {numero} é {sucessor}')
