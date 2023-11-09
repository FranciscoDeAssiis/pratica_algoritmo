# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

#  Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
# sua terça parte.
# Ex:
#   Digite um número: 3.5
#   O dobro de 3.5 é 7.0
#   A terça parte de 3.5 é 1.16666


numero = float(input('Digite um número(real): '))

dobro = numero * 2
terça_parte = numero / 3

print(f'Número: {numero}\nDobro: {dobro}\nTerça Parte: {terça_parte:.4f}.')
