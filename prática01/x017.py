# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
# 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
# o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

velocidade_veículo = float(input('Qual a velocidade do veículo?(Km): '))

if velocidade_veículo > 80:
    valor_multa = (velocidade_veículo - 80) * 5
    print(f'Ultrapassou a velocidade de 80Km. Você foi multado em R${valor_multa:,.2f}!')
else:
    print('Digira com segurança!')

