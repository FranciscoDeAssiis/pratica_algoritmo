# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
# No final, mostre o total de salários pagos aos homens e o total pago às
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
# sempre que ler os dados de um funcionário.

total_salário_homens = total_salário_mulheres = 0

while True:
    print('-'*20)
    salário = float(input('Salário: '))
    sexo = str(input('Sexo: '))

    if sexo == 'm':
        total_salário_homens += salário
    elif sexo == 'f':
        total_salário_mulheres += salário

    continue_loop = str(input('Continuar[n/s]: '))
    if continue_loop == 'n':
        break
    else:
        pass

print(f'{"-"*20}\nTotal pago para homens: R${total_salário_homens:,.2f}\n'
      f'Total pago para mulheres: R${total_salário_mulheres:,.2f}')
