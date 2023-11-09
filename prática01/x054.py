# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
# no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

pessoas = 3
soma_alturas = pessoas_acima_peso_90 = pessoas_peso_50_altura_160 = pessoas_acima_100_altura_190 = 0

for x in range(0, pessoas):
    print(f'{x+1}ª PESSOA: ')
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))

    soma_alturas += altura
    print(soma_alturas)
    if peso > 90:
        pessoas_acima_peso_90 += 1

    if peso < 50 and altura < 1.60:
        pessoas_peso_50_altura_160 += 1

    if altura > 1.90 and peso > 100:
        pessoas_acima_100_altura_190 += 1

media_altura = soma_alturas / pessoas

print(f'Média de altura do grupo: {media_altura}m')
print(f'Total de pessoas acima de 90Kg: {pessoas_acima_peso_90}')
print(f"Total de pessoas com menos de 50Kg e abaixo de 1.60m: {pessoas_peso_50_altura_160}")
print(f'Total de pessoas com mais de 100Kg e acima de 1.90m: {pessoas_acima_100_altura_190}')

