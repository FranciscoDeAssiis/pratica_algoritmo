# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
# aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
# carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
# que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
# quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
# tabela a seguir:
#  - Carros populares (aluguel de R$90 por dia)
#  - Até 100Km percorridos: R$0,20 por Km
#  - Acima de 100Km percorridos: R$0,10 por Km
#  - Carros de luxo (aluguel de R$150 por dia)
#  - Até 200Km percorridos: R$0,30 por Km
#  - Acima de 200Km percorridos: R$0,25 por Km

# Popular:
VALOR_DIARIO_VEÍCULO_POPULAR = 90
POPULAR_ATE_100KM = 0.20
POPULAR_ACI_100KM = 0.10

# Luxuoso:
VALOR_DIARIO_VEÍCULO_LUXUOSO = 150
LUXUOSO_ATE200KM = 0.30
LUXUOSO_ACI200KM = 0.25

total_a_pagar = km_preço = dias_preço = 0

print('Automóvel:\n'
      '[1] - POPULAR\n'
      '[2] - LUXUOSO')
automóvel = str(input('Tipo: ')).lower()
dias_alugados = int(input('Total de dias alugados: '))
km_percorridos = int(input('Total de Km percorridos: '))

if automóvel in ['1', 'popular']:
    if km_percorridos <= 100:
        km_preço = km_percorridos * POPULAR_ATE_100KM
    else:
        km_preço = km_percorridos * POPULAR_ACI_100KM
    dias_preço = dias_alugados * VALOR_DIARIO_VEÍCULO_POPULAR
    total_a_pagar = dias_preço + km_preço
elif automóvel in ['2', 'luxuoso']:
    if km_percorridos <= 200:
        km_preço = km_percorridos * LUXUOSO_ATE200KM
    else:
        km_preço = km_percorridos + LUXUOSO_ACI200KM
    dias_preço = dias_alugados * VALOR_DIARIO_VEÍCULO_LUXUOSO
    total_a_pagar = dias_preço + km_preço

print(f'\n'
      f'Tipo: {automóvel}\n'
      f'Dias: R${dias_preço:,.2f}\n'
      f'Km: R${km_preço:,.2f}\n'
      f'Total: R${total_a_pagar:,.2f}'
      f'\n')
