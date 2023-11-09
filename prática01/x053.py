# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos


person = 5
h = f = s = soma_idades_grupo = media_idades_grupo = soma_idades_homens = total_mulheres_idade_acima = total_homens_cadastrados = total_mulheres_cadastradas = 0

for x in range(0, person):
    print('-'*20)
    nome = str(input('Nome: '))
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))

    soma_idades_grupo += idade

    if sexo.lower() == 'm':
        h += 1
        soma_idades_homens += idade
        total_homens_cadastrados += 1

    elif sexo.lower() == 'f':
        f += 1
        total_mulheres_cadastradas += 1
        if idade >= 20:
            total_mulheres_idade_acima += 1

media_idades_grupo = soma_idades_grupo / person
media_idades_homens = soma_idades_homens / total_homens_cadastrados
print(f'Total de homens cadastrados: {total_homens_cadastrados}')
print(f'Total de mulheres cadastradas: {total_mulheres_cadastradas}')
print(f'Média de idade do grupo: {media_idades_grupo}')
print(f'Média de idade dos homens: {media_idades_homens}')
print(f'Total de mulheres acima de 20 anos: {total_mulheres_idade_acima}')

