# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 29/10/2023
# -------------------------------

# [DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado
# Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos
# termos da sequência serão mostrados na tela. O seu procedimento deve receber
# esse valor e mostrar a quantidade de elementos solicitados.
# Obs: Use os exercícios 70 e 75 para te ajudar na solução
# Ex:
# Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
# Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM

def fibonacci(f):
    a1 = c1 = 0
    b1 = 1
    print(0, end=' >> ')
    for _ in range(f):
        c1 = b1 + a1
        a1 = b1
        b1 = c1
        print(a1, end=' >> ')
    print('FIM')


fibonacci(5)
fibonacci(9)

