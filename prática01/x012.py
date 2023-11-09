# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Crie um programa que leia o preço de um produto, calcule e mostre o seu
# PREÇO PROMOCIONAL, com 5% de desconto.

from random import randint

produtos_tecnologia = [
    ("Smartphone", randint(100, 1000)),
    ("Laptop", randint(100, 1000)),
    ("Tablet", randint(100, 1000)),
    ("Fones de ouvido sem fio", randint(100, 1000)),
    ("Smartwatch", randint(100, 1000)),
    ("Câmera digital", randint(100, 1000)),
    ("Roteador Wi-Fi", randint(100, 1000)),
    ("Impressora a laser", randint(100, 1000)),
    ("Console de videogame", randint(100, 1000)),
    ("Drone", randint(100, 1000))
]
for num, produto in enumerate(produtos_tecnologia):
    print(f'\33[1;34m[{num}]\33[m - \33[1;36m{produto[0]}\33[m, US$: {produto[1]}')

produto = produtos_tecnologia[int(input('\33[1;34mEscolha o índice do produto: \33[m'))]

# Desconto:
desconto = 5 * produto[1] / 100

# Novo preço com desconto:
preço_promocional = produto[1] - desconto

print(f'\33[1;32mO produto {produto[0]} com um desconto de 5%(R${desconto}) tem seu preço reduzido de US${produto[1]:.2f} para US${preço_promocional:.2f}.')
