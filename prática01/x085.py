# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

# Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e
# guarde esses dados em três vetores. No final, mostre uma listagem contendo
# apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.

nomes = []
gêneros = []
salários = []

for x in range(2):
    print(f'{"-"*15} {x + 1}º PESSOA {"-"*15}')
    nomes.append(str(input('Nome: ')).title())
    gêneros.append(str(input('Sexo: ')))
    salários.append(float(input('Salário: ')))

resultados = [(nome, salário) for nome, sexo, salário in zip(nomes, gêneros, salários) if sexo == 'f' and salário > 5000]
for nome, salário in resultados:
    print(f'Nome: {nome}, Salário: R${salário:,.2f}')


#################################################################


resultados = []

for x in range(5):
    print(f'{"-"*15} {x + 1}º PESSOA {"-"*15}')
    nome = str(input('Nome: ')).title()
    sexo = str(input('Sexo: '))
    salário = float(input('Salário: '))

    if sexo == 'f':
        if salário > 500:
            resultados.append((nome, salário))
for nome, salário in resultados:
    print(f'Nome: {nome}, Salário: R${salário:,.2f}')

#################################################################


nomes = []
gêneros = []
salários = []

for x in range(5):
    print(f'{"-"*15} {x + 1}º PESSOA {"-"*15}')
    nomes.append(str(input('Nome: ')))
    gêneros.append(str(input('Sexo: ')))
    salários.append(float(input('Salário: ')))

for x in [n for n, sx in enumerate(gêneros) if sx == 'f']:
    if salários[x] > 5000:
        print(f'Nome: {nomes[x].title()}, Salário: R${salários[x]:,.2f}')

