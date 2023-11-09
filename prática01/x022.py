# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
# situação em relação ao alistamento militar.
#  - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
# alistamento.
#  - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
# alistamento.

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = date.today().year - ano_nascimento

if idade < 18:
    print(f'Faltam {18 - idade} ano(s) para o seu alistamento militar.')
elif idade == 18:
    print(f'Ano para se alistar. Acesse o site para mais informações do dia, local e hora na sua região.')
else:
    print(f'Já se passaram {idade - 18} anos desde o alistamento.')

