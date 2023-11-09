# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
# peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
# indivíduo dentro de certas faixas.
#  - abaixo de 18.5: Abaixo do peso
#  - entre 18.5 e 25: Peso ideal
#  - entre 25 e 30: Sobrepeso
#  - entre 30 e 40: Obesidade
#  - acima de 40: Obseidade mórbida
# Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado
# da altura)

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    info = 'Abaixo do peso.'
elif imc < 25:
    info = 'Peso ideal'
elif imc < 30:
    info = 'Sobrepeso'
elif imc < 40:
    info = 'Obesidade'
else:
    info = 'Obesidade Mórbida'

print(f'{imc:.2f}: {info}')
