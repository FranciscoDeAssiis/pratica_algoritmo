# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
# segundo grau e mostre o valor de Delta.
# exemplos:
#   delta positivo: 4x²-3-1=0
#   delta negativo: 2x²+2+1=0
#   delta igual a 0: x²-10+25=0


from math import sqrt


print('Equação Polinomial Completa')
coeficiente_a = int(input('Termo quadrático(4x²): '))
coeficiente_b = int(input('Termo linear(-3x): '))
coeficiente_c = int(input('Termo constante(-1): '))

real = ''

# fórmula do Discriminante(b²-4.a.c):
delta = (coeficiente_b ** 2) - (4 * coeficiente_a * coeficiente_c)

# Discriminante positivo:
if delta > 0:
    print(f'\33[1;32mDelta {delta}\33[m: Tem duas soluções reais e diferentes.')

    # fórmula de Bhaskara(  ( -b±√(delta) ) / (2.a)  ):
    x1 = (-coeficiente_b + sqrt(delta)) / (2 * coeficiente_a)  # +
    x2 = (-coeficiente_b - sqrt(delta)) / (2 * coeficiente_a)  # -
    print(f'x1= {x1}\nx2= {x2}')

# Discriminante igual a zero:
elif delta == 0:
    print(f'\33[1;32mDelta {delta}\33[m: Há uma única solução real')
    x = -coeficiente_b / (2 * coeficiente_a)
    print(f'x= {x}')

# Discriminante negativo:
elif delta < 0:
    print(f'\33[1;32mDelta {delta}\33[m: Não admite solução real; as raízes são números complexos.')
