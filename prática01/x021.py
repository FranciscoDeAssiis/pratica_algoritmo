# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

#  Faça um algoritmo que leia um determinado ano e mostre se ele é ou não
# BISSEXTO.

from datetime import date


def bissexto(year):
    # 1. Seja divisível por 4. Exemplo: 2000, 2004, 2008, 2012, 2020
    # 2. Seja divisível por 400 (para anos centenários). Exemplo: 1900, 2000, 2100, 2200

    if year % 4 == 0 or year % 400 == 0:
        b = '\33[32mé ano bissexto!'
    else:
        b = '\33[31mnão é ano bissexto!'
    return b


ano = int(input('Digite um ano: '))
print(f'O ano {ano} {bissexto(ano)}')

ano_atual = date.today().year
print(f'\33[mO nosso ano {ano_atual} {bissexto(ano_atual)}')
