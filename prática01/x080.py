# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e
# 15 sorteados pelo computador. Depois disso, peça para o usuário digitar um
# número (chave) e seu programa deve mostrar em que posições essa chave foi
# encontrada. Mostre também quantas vezes a chave foi sorteada.

from random import randrange

vetor = [randrange(1, 15) for x in range(30)]

print(vetor)
chave = int(input('Índice do valor: '))

if chave in vetor:
    índice = vetor.index(chave)
    contagem = vetor.count(chave)
    print(f'Total de ocorrências: {contagem}')
    if contagem > 1:
        índice = [i for i, v in enumerate(vetor) if v == chave]
        print(f'Encontrados nos índices {índice}')
    else:
        print(f'Encontrado no índice {índice}')
else:
    print('O valor não exite no vetor!')

