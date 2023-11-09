# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 28/10/2023
# -------------------------------

# Crie um programa que melhore o procedimento Gerador() da questão anterior
# para que o programador possa escolher uma entre três bordas:
#  +-------=======------+ Borda 1
#  ~~~~~~~~:::::::~~~~~~~ Borda 2
#  <<<<<<<<------->>>>>>> Borda 3
# Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
# ~~~~~~~~:::::::~~~~~~~
#  Portugol Studio
#  Portugol Studio
#  Portugol Studio
# ~~~~~~~~:::::::~~~~~~~


def gerador_título(txt, border_style):
    c = int(len(txt) / 3)
    styles = (('-', '=', '-'), ('~', ':', '~'), ('<', '-', '>'))
    style = tuple
    if border_style == 1:
        style = styles[0]
    elif border_style == 2:
        style = styles[1]
    elif border_style == 3:
        style = styles[2]

    print(f'\33[1;34m+{f"{style[0]}" * c}{f"{style[1]}"*c}{f"{style[2]}"*c}+\33[m')
    print(f'\33[32m{txt}\33[m')
    print(f'\33[1;34m+{f"{style[0]}" * c}{f"{style[1]}"*c}{f"{style[2]}"*c}+\33[m')


txt = 'Crie um programa que melhore o procedimento Gerador() da questão anterior'
gerador_título(txt, 1)
