# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

# Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que mostre uma mensagem personalizada, passada como parâmetro.
# Ex: Ao chamar Gerador("Aprendendo Portugol") aparece:
# +-------=======------+
#  Aprendendo Portugol
# +-------=======------+

def gerador_título(txt):
    c = len(txt)
    print('-' * c)
    print(f'{txt}')
    print('-' * c)


gerador_título('Aprendendo Portugol')
