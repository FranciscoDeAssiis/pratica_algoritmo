# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento
if idade >= 18:
    print('\33[32mPode votar!')
else:
    print('\33[31mNão pode votar!')

print(f'Idade: {idade} anos')
