# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Crie um programa que leia vários números pelo teclado e mostre no final o
# somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

print('Digite "1111" para concluir/sair!')
num = soma = 0
while num != 1111:
    num = int(input('Número: '))
    soma += num
print(f'Soma total: {soma:,.2f}')

