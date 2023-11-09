# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

#  [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

from random import choice

peças = ('pedra', 'papel', 'tesoura')

print('- - - JoKenPo - - -')

print(f'{"-"*20}\n- PEDRA\n- PAPEL\n- TESOURA')
hu = str(input('Escolha: ')).lower()
ma = choice(peças)
resul = 0
if hu in peças:
    if hu == peças[0]:
        if ma == peças[0]:
            resul = 3
        elif ma == peças[2]:
            resul = 1
        elif ma == peças[1]:
            resul = 2

    elif hu == peças[1]:
        if ma == peças[0]:
            resul = 1
        elif ma == peças[1]:
            resul = 3
        elif ma == peças[2]:
            resul = 2

    elif hu == peças[2]:
        if ma == peças[0]:
            resul = 2
        elif ma == peças[1]:
            resul = 1
        elif ma == peças[2]:
            resul = 3

    if resul == 1:
        print(f'Ganhei! a maquína jogou {ma}.')
    elif resul == 2:
        print(f'Perdi! a maquína jogou {ma}.')
    elif resul == 3:
        print(f'Empate! {hu.upper()} vs {ma.upper()}')

else:
    print('Erro de digitação! Escolha entre "pedra", "papel" e "tesoura".')

