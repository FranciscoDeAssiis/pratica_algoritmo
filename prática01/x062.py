# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Faça um programa usando a estrutura “faça enquanto” que leia a idade de
# várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
# não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
# na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

total_de_pessoas = soma_idades = total_pessoas_maiores_21 = 0
while True:
    idade = int(input('Idade: '))
    total_de_pessoas += 1  # Quantas inserções
    soma_idades += idade  # Soma para tirar a média
    if idade >= 21:  # Maiores de 21 anos ou tem 21
        total_pessoas_maiores_21 += 1
    repetição = str(input('Continuar[s/n]: '))
    if repetição == 'n':
        break

medias_idades_grupo = int(soma_idades / total_de_pessoas)

print(f'Total de pessoas: {total_de_pessoas}\n'
      f'Média das idades: {medias_idades_grupo}\n'
      f'Maíores de 21 anos: {total_pessoas_maiores_21}')
