listNum = [[], []] # <-- Lista contendo outras duas lista para 
# armazenar os valore PARES e IMPARES.

num = 0 
for i in range(1, 8):          # <-- Vai gerar oito inputs para ser digitado os números.
    num = int(input(f'Digite o {i} valor: ')) # <-- Variavel num vai ser o "separador" de PARES e IMPARES.
    if num % 2 == 0:           # <-- Condição que vai verificar se o número digitado tem o resto da divisão por 0 
        listNum[0].append(num) # <-- se for verdade irai adicionar na lista [0][0].
    else:                      # <-- Se não vai acrecentar na lista [0][1]
        listNum[1].append(num)

print('*' * 40)
listNum[0].sort() # <-- Vai ordenar em ordem crescente os valores PARES.
listNum[1].sort() # <-- Vai ordenar em ordem crescente os valores IMPARES.
print(f'Os valores PARES digitados foram: {listNum[0]}')
print(f'Os valores IMPARES digitados foram: {listNum[1]}')
