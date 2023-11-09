# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#  - Média até 4.9: REPROVADO
#  - Média entre 5.0 e 6.9: RECUPERAÇÃO
#  - Média 7.0 ou superior: APROVADO

aluno = str(input('Aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media > 6.9:
    print('\33[32mAprovado!\33[m')
elif media > 4.9:
    print('\33[33mRecuperação!\33[m')
else:
    print('\33[31mReprovado!\33[m')
