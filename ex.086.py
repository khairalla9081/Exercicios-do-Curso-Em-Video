matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3): # LINHA DA MATRIZ
    for j in range(0, 3): # COLUNA DA MATRIZ
        matriz[i][j] = int(input(f'Digite um valor para [{i},{j}]: '))
        # VARIAVEL[LINHA][COLUNA]

print('-=' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()  
