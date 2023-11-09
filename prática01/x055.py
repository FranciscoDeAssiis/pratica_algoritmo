# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
# agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
# tentativas para tentar acertar.

from random import randint


numero_sorteado = randint(1, 10)
for x in range(4, 0, -1):
    palpite = int(input(f'Chances: {x}ª. Palpite: '))
    if palpite == numero_sorteado:
        print(f'Você acertou! O número sorteado foi {numero_sorteado}!')
        break
    else:
        if x == 1:
            print('Perdeu todas as chances!')
        else:
            print('Você errou!')