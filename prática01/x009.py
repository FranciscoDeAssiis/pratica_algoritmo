# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

# Importações:
import json
import requests
import threading
import time

dollar = float()


# Dollar atual:
def dollarAPI():
    # API Cotação do dollar em tempo real:
    api = "https://economia.awesomeapi.com.br/last/USD-BRL"  # USD-BRL,EUR-BRL,BTC-BRL
    global dollar
    dollar = float(requests.get(api).json()['USDBRL']['bid'])


# threading para requisição do dollar atual:
threading.Thread(target=dollarAPI).start()

# Digitação do dinheiro em real:
real = float(input('Dinheiro(R$): '))

# conversão de real para dollar:
real_pra_dollar = real / dollar

# exibindo conversão de real para dollar:
print(f'\nCom \33[1;32mR${real:.2f}\33[m, consegue comprar \33[1;36mUS${real_pra_dollar:,.2f}\33[m.')
