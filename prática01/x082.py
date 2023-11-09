# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 27/10/2023
# -------------------------------


# Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em
# um vetor. No final, mostre:
# a) Qual é a média da turma
# b) Quantos alunos estão acima da média da turma
# c) Qual foi a maior nota digitada
# d) Em que posições a maior nota aparece

alunos_notas = []
alunos_media = []
alunos_acima = 0
turma_media = 0
maior_nota = 0
soma = 0
maior_nota_posição = ''
for x in range(10):
    vetor = []
    print(f"{'-'*15} {x+1}º ALUNO {'-'*15}")
    vetor.insert(0, float(input('Primeira Nota: ')))
    vetor.insert(1, float(input('Segunda Nota: ')))
    alunos_notas.append(vetor)
    alunos_media.append((vetor[0] + vetor[1]) / 2)

turma_media = sum(alunos_media) / len(alunos_media)

for x in alunos_media:
    if x > turma_media:
        alunos_acima += 1

for cx, x in enumerate(alunos_notas):
    for ci, i in enumerate(x):
        if cx == 0:
            maior_nota = i
            maior_nota_posição = f'Lista: í{cx}; índice: í{ci}'
        elif i > maior_nota:
            maior_nota = i
            maior_nota_posição = f'Lista: í{cx}; índice: í{ci}'

print(f'Média da turma: {turma_media:.1f}\n'
      f'Alunos acima da média da turma: {alunos_acima}\n'
      f'A maior nota digitada: {maior_nota}\n'
      f'Posição onde a maior nota aparece: {maior_nota_posição}')
print(alunos_notas)

