# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

# [DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números
# aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os
# números gerados e depois coloque o vetor em ordem crescente, mostrando no final
# os valores ordenados.

from random import randrange



# Bubble Sort:
# Um algoritmo simples que compara pares de elementos adjacentes e os troca se estiverem
# na ordem errada. O processo é repetido até que a lista esteja ordenada.
vetor = []
for x in range(20):
    vetor.append(randrange(0, 99))
print(vetor)
for i in range(len(vetor)):
    for x in range(len(vetor)-1):
        if vetor[x] > vetor[x+1]:
            _ = vetor[x]
            vetor[x] = vetor[x+1]
            vetor[x+1] = _
print(vetor)


# Selection Sort:
# Este algoritmo seleciona o elemento mínimo da lista e o move para a posição correta.
# Isso é feito repetidamente até que a lista inteira esteja ordenada.
print('\n\n')
vetor = []
for x in range(20):
    vetor.append(randrange(0, 99))
print(vetor)
# Entrada: [42, 51, 76, 13, 27, 94, 48, 53, 86, 61, 62, 35, 63, 10, 18, 7, 8, 83, 56, 29]
for i1, num1 in enumerate(vetor):
    for i2, num2 in enumerate(vetor):
        if num1 < num2:
            vetor[i1] = num2
            vetor[i2] = num1
            num1 = num2
print(vetor)
# Saída: [7, 8, 10, 13, 18, 27, 29, 35, 42, 48, 51, 53, 56, 61, 62, 63, 76, 83, 86, 94]


# Insertion Sort:
# Neste algoritmo, a lista é dividida em uma parte ordenada e uma parte não ordenada.
# Elementos da parte não ordenada são inseridos na parte ordenada na posição apropriada.
print('\n\n')
vetor = []
for x in range(20):
    vetor.append(randrange(0, 99))
print(vetor)

for índice in range(1, len(vetor)):
    valor_do_índice = vetor[índice]  # ex:v 6 Pega o valor posicionado no índice 'i'. Índice começa no 1.
    índice_anterior = (índice - 1)  # ex:í 0 Pega o índice anterior. No inicio, pega o primeiro índice '0'.

    # Enquanto índice anterior for maior e VALOR do índice anterior for MAIOR QUE o VALOR do próximo índice, faça:
    while índice_anterior >= 0 and vetor[índice_anterior] > valor_do_índice:
        # Adiciona valor do índice anterior no próximo índice:
        vetor[índice_anterior + 1] = vetor[índice_anterior]  # ex:índice 1 = índice 0
        # Volta 1 índice e recomeça o loop até o índice 0:
        índice_anterior -= 1  # ex: índice 14 -> índice 13

    # ex:6
    print(vetor[índice_anterior + 1], valor_do_índice)
    vetor[índice_anterior + 1] = valor_do_índice

print(vetor)


###########################################################################################
###########################################################################################

def merge_sort(lista):
    if len(lista) > 1:
        # Divide a lista em duas metades
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        # Recursivamente ordena as duas metades
        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        # Mescla as duas metades ordenadas
        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1


# Exemplo de uso
lista = [12, 11, 13, 5, 6, 7]
merge_sort(lista)
print("Lista ordenada:", lista)


###########################################################################################
###########################################################################################


def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Se a lista tiver 0 ou 1 elemento, ela já está ordenada.

    # Escolhe um elemento pivot (pode ser o primeiro, último, do meio, etc.)
    pivot = lista[len(lista) // 2]

    # Divide a lista em três partes: elementos menores que o pivot, iguais ao pivot e maiores que o pivot
    menores = [x for x in lista if x < pivot]
    iguais = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]

    # Recursivamente ordena as partes menores e maiores
    return quick_sort(menores) + iguais + quick_sort(maiores)

# Exemplo de uso
lista = [12, 11, 13, 5, 6, 7]
lista_ordenada = quick_sort(lista)
print("Lista ordenada:", lista_ordenada)




