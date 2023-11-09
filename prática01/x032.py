# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
# jogador vai tentar descobrir qual foi o valor sorteado.

from random import randint


while True:
    num_sorteado = randint(1, 5)
    cont = 0
    print('-' * 60)

    while True:
        esc = int(input('Escolha o número entre 1 e 5: '))
        cont += 1
        if esc == num_sorteado:
            print(f'Você acertou! o número sorteado foi {num_sorteado}.')
            print(f'Total de tentativas: {cont}')
            break
        elif esc < num_sorteado:
            print('O número sorteado é maior.')
        else:
            print('O número sorteado é menor.')

