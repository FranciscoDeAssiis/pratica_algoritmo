# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Faça um programa que leia a largura e o comprimento de um terreno
# retangular, calculando e mostrando a sua área em m². O programa também
# deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
#  - Abaixo de 100m² = TERRENO POPULAR
#  - Entre 100m² e 500m² = TERRENO MASTER
#  - Acima de 500m² = TERRENO VIP

largura = float(input('Largura: '))
altura = float(input('Altura: '))

area = largura * altura

if area <= 100:
    classificação = 'TERRENO POPULAR'
elif area <= 500:
    classificação = 'TERRENO MASTER'
else:
    classificação = 'TERRENO VIP'

print(f'Classificação do terreno: {classificação}')
print(f'Área total: {area:.2f}²')
