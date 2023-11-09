# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
# qualquer e mostre uma contagem até esse valor:
# Ex: Digite um valor: 35
# Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!

num = int(input('Digite um número: '))

for i in range(1, num+1):
    print(i, end=' ')
    if i == num:
        print('Acabou!')

i = 1
while i <= num:
    print(i, end=' ')
    i += 1
    if i == num + 1:
        print('Acabou!')
