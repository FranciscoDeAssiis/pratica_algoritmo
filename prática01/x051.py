# ------------------------------
# Autor: Francisco de Assis
# Instagram: @rarodsg
# Local:
# Data: 26/10/2023
# -------------------------------

# Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
# qual foi o maior e qual foi o menor preço digitados.

maior = menor = penúltimo_maior = penúltimo_menor = 0
for x in range(0, 8):
    preço = float(input(f'Digite o peço do {x+1}º produto: '))

    if x == 0:
        maior = menor = preço

    if preço > maior:
        penúltimo_maior = maior
        maior = preço

    if preço < menor:
        penúltimo_menor = menor
        menor = preço

print(f'O maior valor digitado foi {maior:.2f}')
print(f'O penúltimo maior: {penúltimo_maior}')
print(f'O menor valor digitado foi {menor:.2f}')
print(f'O penúltimo menor: {penúltimo_menor}')

