# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
# Analise seus comprimentos e diga se é possível formar um triângulo com essas
# retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
# de cada lado deve ser menor que a soma dos outros dois.

print("Desigualdade Triangular.")
seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))

if seg3 <= (seg1 + seg2) and seg1 <= (seg2 + seg3) and seg2 <= (seg1 + seg3):
    print('\33[32mPode formar um triângulo!')
else:
    print('\33[31mNão formam um triângulo!')
    if not seg1 < (seg3 + seg2):
        print(f'O seguimento {seg1} é maior que a soma dos outros.')
    if not seg2 < (seg1 + seg3):
        print(f'O seguimento {seg2} é maior que a soma dos outros.')
    if not seg3 < (seg1 + seg2):
        print(f'O seguimento {seg3} é maior que a soma dos outros.')
