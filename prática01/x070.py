# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------

#  [DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência
# de Fibonacci:
# 1 1 2 3 5 8 13 21...


# Cada número é a soma dos dois anteriores
# Em termos matemáticos, a sequência é definida pela fórmula
# Fn = fn-1 + Fn-2,
# sendo o primeiro termo F1 = 1 e os valores iniciais F1 = 1, F2 = 1.
# Esse método é aplicado na análise de mercados financeiros,
# na teoria de jogos e na ciência da computação, além de configurações biológicas e naturais.
a1 = 0
b1 = 1
c1 = 0
print(a1, end=',     ')  # Start inicial
for x in range(0, 20):
    c1 = a1 + b1  # depende dos dois anteriores para gerar o terceiro
    a1 = b1  # recebe o valor afrente
    b1 = c1  # recebe o valor afrente

    print(a1, end=', ')  # começa com 1
