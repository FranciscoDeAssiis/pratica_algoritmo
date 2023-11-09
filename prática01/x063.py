# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa usando a estrutura “faça enquanto” que leia vários números.
# A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
# tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares


soma = menor_número = media_números = total_pares = total_números = 0
while True:
    num = float(input('Número: '))

    soma += num
    total_números += 1

    if menor_número == 0:
        menor_número = num
    elif num < menor_número:
        menor_número = num

    if num % 2 == 0:
        total_pares += 1

    repetir = int(input('Continuar[0/1]: '))
    if not repetir:
        media_números = soma / total_números
        break
    else:
        print('-' * 30)

print(f'Soma total: {soma:,.2f}\n'
      f'Menor valor: {menor_número:,.2f}\n'
      f'Média: {media_números:,.2f}\n'
      f'Total pares: {total_pares}')
