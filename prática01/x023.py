# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
# para todos, mas especialmente para mulheres. Faça um programa que leia nome,
# sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
# que:
#  - Homens ganham 5% de desconto
#  - Mulheres ganham 13% de desconto

cliente = {'nome': str(input('Seu nome: ')),
       'sexo': str(input('Seu sexo: ')),
       'preç': float(input('Valor total das compras: '))}

DESM = 5  # desconto para homens
DESF = 13  # desconto para mulheres

if cliente['sexo'].lower() in ['f', 'feminino']:
    novo_preço = cliente['preç'] - (DESF * cliente['preç'] / 100)
    print(f'Desconto de {DESF}%!', end=' ')
else:
    novo_preço = cliente['preç'] - (DESM * cliente['preç'] / 100)
    print(f'Desconto de {DESM}%!', end=' ')

print(f'De R${cliente["preç"]:,.2f} por apenas R${novo_preço:,.2f}!')
cliente['preç'] = novo_preço
