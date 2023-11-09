# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos
pessoa_mais_velha = \
    idade_pessoa_mais_velha = \
    media_idade_grupo = \
    total_homens_mais_30 = \
    total_mulheres_menos_18 = \
    idade_mulher_mais_jovem = \
    soma_idades_grupo = total_de_pessoas = 0
nome_mulher_mais_jovem = \
    nome_pessoa_mais_velha = ''

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))

    soma_idades_grupo += idade
    total_de_pessoas += 1

    if idade_pessoa_mais_velha == 0:
        nome_pessoa_mais_velha = nome
        idade_pessoa_mais_velha = idade
    elif idade > idade_pessoa_mais_velha:
        nome_pessoa_mais_velha = nome
        idade_pessoa_mais_velha = idade

    if sexo == 'f':
        if idade_mulher_mais_jovem == 0:
            nome_mulher_mais_jovem = nome
            idade_mulher_mais_jovem = idade

        elif idade < idade_mulher_mais_jovem:
            idade_mulher_mais_jovem = idade

        if idade < 18:
            total_mulheres_menos_18 += 1

    elif sexo == 'm':
        if idade > 30:
            total_homens_mais_30 += 1

    repetir = str(input('Continuar?[s/n]: '))
    if repetir == 'n':
        break
    else:
        print('-'*30)

media_idade_grupo = soma_idades_grupo / total_de_pessoas

print(f'\n'
      f'Pessoa mais velha: {nome_pessoa_mais_velha.title()} com {idade_pessoa_mais_velha} anos\n'
      f'Mulher mais jovem: {nome_mulher_mais_jovem.title()} com {idade_mulher_mais_jovem} anos\n'
      f'Média de idade do grupo: {media_idade_grupo:.0f}\n'
      f'Homens com mais de 30 anos: {total_homens_mais_30}\n'
      f'Mulheres com menos de 18 anos: {total_mulheres_menos_18}')
