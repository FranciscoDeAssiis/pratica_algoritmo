# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
#  - EQUILÁTERO: todos os lados iguais
#  - ISÓSCELES: dois lados iguais
#  - ESCALENO: todos os lados diferentes

print("Desigualdade Triangular.")
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 <= (r2 + r3) and r2 <= (r1 + r3) and r3 <= (r1 + r2):
    print('Forma triângulo!')
    # Equilátero:
    if r1 == r2 and r2 == r3:
        print('    - tipo equilátero')
    # Escaleno:
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('    - tipo escaleno')
    # Isósceles:d
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('    - tipo isósceles')

else:
    msg1 = 'não forma triângulo'
