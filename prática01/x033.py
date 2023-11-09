# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Escreva um programa para aprovar ou não o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_imóvel = float(input('Valor do imóvel: '))
salario_comprador = float(input('Salário do comprador: '))
anos_quitação = int(input('parcelar em quantos anos: '))

parcelas_mensais_imovel = valor_imóvel / (anos_quitação * 12)

valor_limite_parcelas = 30 * salario_comprador / 100

if parcelas_mensais_imovel < valor_limite_parcelas:
    print(f'Empréstimo confirmado! o parcelamente de R${parcelas_mensais_imovel:,.2f} está abaixo do valor limite de R${valor_limite_parcelas:,.2f} ')
else:
    print(f'Empréstimo negado! o parcelamento de R${parcelas_mensais_imovel:,.2f} está acima do valor limite de R${valor_limite_parcelas:,.2f}')

print(f'Prestação: {parcelas_mensais_imovel:,.2f}\n'
      f'Limite: {valor_limite_parcelas:,.2f}\n'
      f'Meses: {anos_quitação * 12}')
