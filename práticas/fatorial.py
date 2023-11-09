# Exemplo:
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 3 x 1 = 120

# O fatorial de um número natural (n) é o produto dos números naturais de 1 até (n) representado por (n!).
# O fatorial é basicamente um produto de números naturais consecutivos até chegar ao número desejado.

# Atenção:
#   0! = 1
#   1! = 1

# 0!
#   A ideia aqui é que 0! representa o produto de nenhum número.
#   Imagina que você tem uma lista vazia de coisas para multiplicar. O resultado é 1 porque, em temos práticos,
#   não há nenhum número para multiplicar. É como se fosse o "elemento neutro" da multiplicação.
#
# 1!
#   Agora, 1! é o produto de apenas um número, que é 1.
#   Se você tem apenas um item para multiplicar(no caso, o número 1), o resultado é esse número em si.
#
# Isso é feito para manter consistência em várias fórmulas matemáticas.
# É útil em contextos mais avançados, como séries de Taylor.
# Quando calculamos fatoriais, é como se estivéssemos multiplicando um número pelos seus antecessores até chegar em 1.
# Ignoremos o próprio número e multipliquemos apenas os números menores até chegar em 1.

# Calculo:
# n! = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5)...
# n! = n * (n - 1)


# Para cada interação é retirado 1 do (n!) até (n!) seja igual a 1.


# Parte 1: ---------------------------------------------------------------------
print('Parte 1', '-'*20)

for n in range(1, 5+1):
    print(f'{n}!')


# Parte 2: ---------------------------------------------------------------------
print('\nParte 2', '-'*20)

fatorial = 1  # 1! = 1
for n in range(1, 5+1):
    produto = fatorial * n
    print(produto)


# Parte 3: ---------------------------------------------------------------------
print('\nParte 3', '-'*20)
fatorial = 1  # 1! = 1
for n in range(1, 5+1):
    # n * (n - 1)
    # n * n
    fatorial = fatorial * n
    print(fatorial)


# Parte 4: ---------------------------------------------------------------------
print('\nParte 4', '-'*20)


def fatorial(num):
    fat = 1  # 1! = 1
    total = 0
    for n in range(1, num + 1):
        # n * (n - 1)
        # n * n
        fat = fat * n
    return fat


fatorial = fatorial(5)
print(fatorial)
