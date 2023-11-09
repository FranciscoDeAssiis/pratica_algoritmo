# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 29/10/2023
# -------------------------------

# Crie uma lógica que leia um número inteiro e passe para um procedimento
# ParOuImpar() que vai verificar e mostrar na tela se o valor passado como
# parâmetro é PAR ou ÍMPAR.

def par_ou_impar(num: int):
    if num % 2 == 0:
        return 'PAR'
    return 'ÍMPAR'

