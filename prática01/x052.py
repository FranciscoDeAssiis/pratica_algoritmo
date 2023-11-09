# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

#  Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

acima_18 = maior_idade = menor_idade = soma_idades = s = 0
persons = 10
for x in range(0, persons):
    idade = int(input(f'Idade da {x+1}º pessoa: '))

    soma_idades += idade

    if x == 0:
        maior_idade = idade

    if idade >= 18:
        acima_18 += 1
        if idade > maior_idade:
            maior_idade = idade

    elif idade <= 5:
        menor_idade += 1

media_grupo = soma_idades / persons

print(f'Média do grupo: {media_grupo}')
print(f'Maiores de 18 anos: {acima_18}')
print(f'Menos de 5 anos: {menor_idade}')
print(f'A maior idade: {maior_idade}')

