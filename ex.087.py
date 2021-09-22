# 1 - Somar todos os valores PARES digitados ----
# 2 - Somar todos os valores da TERCEIRA coluna ---
# 3 - O MAIOR valor da SEGUNDA linha ----
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:        
            pares += matriz[l][c]
    coluna += matriz[l][2]
    print()

print(f'A soma de todos os pares: {pares}')
print(f'A soma dos valores da terceira coluna é: {coluna}')
print(f'O maior valor da segunda coluna é: {max(matriz[1])} ')

