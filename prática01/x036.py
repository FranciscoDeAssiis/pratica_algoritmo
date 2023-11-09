# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 25/10/2023
# -------------------------------

# Um programa de vida saudável quer dar pontos de atividades físicas que podem
# ser trocados por dinheiro. O sistema funciona assim:
#  - Cada hora de atividade física no mês vale pontos
#  - até 10h de atividade no mês: ganha 2 pontos por hora
#  - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
#  - acima de 20h de atividade no mês: ganha 10 pontos por hora
#  - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês,
# calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

horas_total_mes = float(input('Total de horas de atividade física no mês: '))

if horas_total_mes < 10:
    pontos = horas_total_mes * 2

elif horas_total_mes < 20:
    pontos = horas_total_mes * 5

else:
    pontos = horas_total_mes * 10

ganhos = pontos * 0.05

print(f'Pontos: {pontos:.2f}\n'
      f'Ganhos: R${ganhos:,.2f}')
