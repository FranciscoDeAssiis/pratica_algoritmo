# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 29/10/2023
# -------------------------------

# Faça um programa que tenha um procedimento chamado Contador() que recebe
# três valores como parâmetro: o início, o fim e o incremento de uma contagem. O
# programa principal deve solicitar a digitação desses valores e passá-los ao
# procedimento, que vai mostrar a contagem na tela.

def contador(ini, fin, inc):
    for x in range(ini, fin+1, inc):
        if not x == fin:
            print(x, end=', ')
        else:
            print(x)


contador(1, 10, 1)

