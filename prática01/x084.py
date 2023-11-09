# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

#  Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses
# valores em dois vetores, em posições relacionadas. No final, mostre uma listagem
# contendo apenas os dados das pessoas menores de idade.

nomes = []
idades = []

for x in range(9):
    print(f'{"-"*15} {x + 1}º PESSOA {"-"*15}')
    nomes.append(str(input('Nome: ')))
    idades.append(int(input('Idade: ')))

idades_menores = [idades[x] for x in [n for n, idade in enumerate(idades) if idade < 18]]
nomes_menos = [nomes[x].title() for x in [n for n, idade in enumerate(idades) if idade < 18]]

for x in range(len(nomes_menos)):
    print(f'Idade: {idades_menores[x]} - Nome: {nomes_menos[x]}')

