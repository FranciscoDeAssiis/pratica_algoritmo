# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

cont = menor_idade_mulher = total_homens_cadastrados = soma_idades_homens = media_idade_homens = 0

while True:
    print('-' * 30)
    sexo = str(input('Sexo: '))
    idade = int(input('Idade: '))

    if cont == 0:
        maior_idade = idade

    if sexo == 'f':
        if not menor_idade_mulher:
            menor_idade_mulher = idade
        elif idade < menor_idade_mulher:
            menor_idade_mulher = idade

    elif sexo == 'm':
        total_homens_cadastrados += 1
        soma_idades_homens += idade

    cont += 1
    res = str(input('Continuar?[s/n]: '))
    if res == 'n':
        break


if total_homens_cadastrados:
    media_idade_homens = int(soma_idades_homens / total_homens_cadastrados)

print(f'\n'
      f'Total de homens cadastrados: {total_homens_cadastrados}\n'
      f'Idade da mulher mais jovem: {menor_idade_mulher}\n'
      f'Méida de idade dos homens cadastrados: {media_idade_homens}')
