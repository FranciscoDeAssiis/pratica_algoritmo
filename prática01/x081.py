# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No
# final, mostre:
# a) Qual é a média de idade das pessoas cadastradas
# b) Em quais posições temos pessoas com mais de 25 anos
# c) Qual foi a maior idade digitada (aceita repetições)
# d) Em que posições digitamos a maior idade

idades = [int(input(f'{x}º Idade: ')) for x in range(8)]

media_idades = sum(idades) / len(idades)  # Média das idades
acima_25 = [i for i, v in enumerate(idades) if v > 25]  # índices das idades acima de 25
maior_idade = max(idades)
índice_maior_idade = idades.index(maior_idade)

print(f'Média de idade das pessoas: {media_idades:.0f}\n'
      f'Índice das pessoas maiores de 25 anos: {acima_25}\n'
      f'Maior idade digitada: {maior_idade}\n'
      f'Índice/posição da maior idade: {índice_maior_idade}\n')
