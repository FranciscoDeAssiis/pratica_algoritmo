# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

#  Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos
# existem na turma e qual é a média de idade do grupo.

soma_idades = total_alunos = 0
while True:
    idade = int(input('Idade: '))

    if idade == 999:
        break

    soma_idades += idade
    total_alunos += 1

media_idade_alunos = soma_idades / total_alunos

print(f'Total de alunos na turma: {total_alunos}\n'
      f'Média de idade da turma: {media_idade_alunos:.1f}')
