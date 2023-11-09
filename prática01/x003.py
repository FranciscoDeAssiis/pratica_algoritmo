# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Crie um programa que leia o nome e o salário de um funcionário, mostrando uma mensagem no final.
# Ex:
#   Nome do Funcionário: Maria do Carmo
#   Salário: 1850,45
#   O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

data = ('Terça-Feira', 'Outubro', 2023)

nome_funcionario = str(input('Nome: '))
salario_funcionario = float(input('Salário: '))

print(f'O funcionario \33[33m{nome_funcionario}\33[m tem um salário de \33[32mR${salario_funcionario:.2f}\33[m em {data[1]}.')

