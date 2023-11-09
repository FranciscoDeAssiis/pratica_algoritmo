# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

#  Desenvolva um programa que leia uma distância em metros e mostre os valores
# relativos em outras medidas.
# Ex:
#   Digite uma distância em metros: 1000


m = float(input('Distância(m): '))

# Quilômetro (km)
km = m / 1000
# Hectômetro (hm)
hm = m / 100
# Decâmetro (dam)
dam = m / 10
# Decímetro (dm)
dm = m * 10
# Centímetro (cm)
cm = m * 100
# Milimétro (mm)
mm = m * 1000

unidades = [('Quilômetro', km),
            ('hectômetro', hm),
            ('Decâmetro', dam),
            ('Decímetro', dm),
            ('Centímetro', cm),
            ('Milimétro', mm)]

for unidade in unidades:
    print(f'\33[36m{unidade[0]:<10}\33[m \33[32m{unidade[1]:.2f}\33[m')
