# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

# Melhore o exercício 96, criando além da função Media() uma outra função
# chamada Situacao(), que vai retornar para o programa principal se o aluno está
# APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como
# parâmetro o resultado retornado pela função Media().

def media(n1: [int, float], n2: [int, float]) -> float:
    return float((n1 + n2) / 2)


def situação(m):
    if m > 7:
        return '\33[1;32mAPROVADO\33[m'
    elif m > 5:
        return '\33[1;33mRECUPERAÇÃO\33[m'
    else:
        return '\33[1;31mREPROVADO\33[m'


m = media(6, 8.5)
print(situação(m))
m = media(6, 5)
print(situação(m))
m = media(5, 5)
print(situação(m))

