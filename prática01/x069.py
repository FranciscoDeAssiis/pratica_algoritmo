# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# [DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e
# a soma entre todos os valores da sequência.


#########################################

# Progressão Aritmética Crescente = R > 0
# Progressão Aritmética Decrescente = R < 0
# Progressão Aritmética Constante = R = 0
# Termo geral: an = a1 + (n - 1) . r

# an -> enésimo termo. n -> índice
# a1 -> Primeiro termo
# n = nº de termos
# r -> razão da PA

# Ex: an  = a1 + (n - 1)  . R
# Ex: a21 = 10 + (21 - 1) . 4

# Soma da PA:
# sn = (a1 + an) / 2

# sn -> Soma
# a1 -> 1º
# an -> último termo
# n -> nº de termos


# a1 = int(input('Primeiro termo: '))
# r = int(input('Razão: '))

# a30 = 1 + (30 - 1) . 2
# a30 = 59  # total na camada 30º

# 1, 3, 5, ... a30
# a1           59

# s = ((1 + a30) . 30) / 2
# s = ((1 + 59) . 30) / 2
# no total, do primeiro(1º) termo até o temo 30º tem 900

a1 = 31
an = n = 147
r = 3

a147 = 31 + (147-1) * r  # 469
somaPA = (a1 + a147) * 147 / 2  # 36750

print(f'a1: {a1}\n'
      f'an: {an}\n'
      f'r: {r}\n')

print('\33[32mTERMO GERAL DA P.A: \33[m')
print('\33[34ma\33[36mn\33[m = a1 + (\33[36mn\33[m - 1) * r')
print(f'A camada {an}ª tem o valor {a147}\n')

print('\33[32mSOMA DA P.A: \33[m')
print('s\33[33mn\33[m = (a1 + \33[34ma\33[36mn\33[m) . \33[33mn\33[m')
print(f's\33[33m{n}\33[m = ({a1} + \33[34m{a147}\33[m) * \33[33m{n}\33[m')
print(f'Da camada {a1}ª até a camada {an}ª, a soma de todas as camadas é {somaPA}')

print('-----------------')


a = int(input('Primeiro termo: '))
enesimo = 10
r = int(input('Razão: '))
for x in range(a, a + enesimo):
    print(a, end=' ')
    a = a + r

print()

for x in range(a, a + enesimo, r):
    print(x, end=' ')

print()

# an = a1 + (n -1) . r
a1 = 2
n = 10
r = 3
an = a1 + (n - 1) * r
print(an)

print('--------')

# an = a1 + (n -1) . r
a1 = 2
n = 10
r = 3
print(a1)
for n in range(a1, a1 + 9):
    an = a1 + (n - 1) * r
    print(an)

# valorTermoÍndice = primeiroTermo + (índice - 1) * razão

