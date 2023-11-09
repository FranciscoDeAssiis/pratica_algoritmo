# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Uma empresa precisa reajustar o salário dos seus funcionários, dando um
# aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
# o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
# No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
#  - menos de 15 anos de empresa: +5%
#  - de 15 até 20 anos de empresa: +12%
#  - mais de 20 anos de empresa: +23%
# - Homens
#  - menos de 20 anos de empresa: +3%
#  - de 20 até 30 anos de empresa: +13%
#  - mais de 30 anos de empresa: +25%

salário = float(input('Salário: '))
sexo = str(input('Gênero[f/m]: '))
anos_na_empresa = int(input('Total de anos na empresa: '))
reajuste = 0  # +0%

if sexo in ['f', 'feminino']:
    if anos_na_empresa < 15:
        reajuste = 5
    elif anos_na_empresa < 20:
        reajuste = 12
    else:
        reajuste = 23

elif sexo in ['m', 'masculino']:
    if anos_na_empresa < 15:
        reajuste = 3
    elif anos_na_empresa < 20:
        reajuste = 13
    else:
        reajuste = 25

reajuste_salarial = salário + (reajuste * salário / 100)

print(f'Reajuste salárial(+{reajuste}%): R${reajuste_salarial:,.2f}')
# print(reajuste * salário / 100)
