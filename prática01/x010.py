# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Faça um algoritmo que leia a largura e altura de uma parede, calcule e
# mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
# sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura = float(input('Largura da parede(m): '))
altura = float(input('Altura da parede(m): '))

area_total = largura * altura
latas = round(area_total / 2)  # arredonda para cima para preencher o desperdício de tinta durante a pintura.

print(f'Necessário {latas} latas para pintar uma área de {area_total}m².')
