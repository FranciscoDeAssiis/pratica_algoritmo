# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
# “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

total_mulheres_cadastradas = \
    total_peso_mulheres = \
    total_homens_peso_acima_100 = \
    media_peso_mulheres = \
    maior_peso_homem = 0

total_pessoas = 8  # total de pessoas para cadastro
for x in range(1, total_pessoas+1):
    sexo = str(input('Sexo: '))
    peso = float(input('Peso: '))

    if sexo == 'f':
        total_mulheres_cadastradas += 1  # Total de mulheres
        total_peso_mulheres += peso  # Somando os kg de cada mulher cadastrada

    elif sexo == 'm':
        if maior_peso_homem == 0:  # Homem mais pesado
            maior_peso_homem = peso
        elif peso > maior_peso_homem:
            maior_peso_homem = peso

        if peso > 100:  # Homens acima de 100Kg
            total_homens_peso_acima_100 += 1

    if x == total_pessoas:  # Média entre as mulheres
        media_peso_mulheres = total_peso_mulheres / total_mulheres_cadastradas

print(f'Total de mulheres cadastradas: {total_mulheres_cadastradas}\n'
      f'Total homens acima de 100Kg: {total_homens_peso_acima_100}\n'
      f'Média de peso entre as mulhesres: {media_peso_mulheres:.2f}Kg\n'
      f'Maior peso entre os homens: {maior_peso_homem:.2f}Kg')

