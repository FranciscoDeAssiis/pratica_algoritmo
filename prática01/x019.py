# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 24/10/2023
# -------------------------------

# Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
# média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
# não um bom aproveitamento (se ficou acima da média 7.0).

nome = str(input('NOME DO ALUNO: '))
nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))

media = (nota1 + nota2) / 2

print(f'A média de {nome} foi {media}.', end=' ')
if media > 7:
    print('Aprovado!')
elif media > 5:
    print('Recuperação!')
else:
    print('Reprovado!')
