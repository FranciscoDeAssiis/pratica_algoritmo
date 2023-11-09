# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
#  - Até 3 anos de empresa: aumento de 3%
#  - entre 3 e 10 anos: aumento de 12.5%
#  - 10 anos ou mais: aumento de 20%

nome = str(input('Nome: '))
sl = float(input('Salário(R$): '))
anos = int(input('Anos na empresas: '))
r = 0

if anos == 3:
    r = 3
elif 3 <= anos <= 10:
    r = 12.5
elif anos > 10:
    r = 20

sl = sl + (r * sl / 100)

print(f'Aumento de {r}%. Reajustado para R${sl:,.2f}.')
