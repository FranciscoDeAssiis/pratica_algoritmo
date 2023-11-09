# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

# Crie um programa que melhore o procedimento Gerador() da questão anterior,
# Recebendo um parâmetro de repetição de texto.
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======------+
#  Aprendendo Portugol
#  Aprendendo Portugol
#  Aprendendo Portugol
#  Aprendendo Portugol
# +-------=======------+

def gerador_títulos(txt: str, r=1) -> None:
    c = len(txt)
    print('-' * c)
    for _ in range(r):
        print(txt)
    print('-' * c)


gerador_títulos('Arpendendo Portubol', 4)
