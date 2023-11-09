# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 29/10/2023
# -------------------------------

# Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma
# adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o
# maior entre eles.

def maior(*args):
    return max(args)


maior = maior(3, 5, 7)
print(f'O maior número é {maior}')

