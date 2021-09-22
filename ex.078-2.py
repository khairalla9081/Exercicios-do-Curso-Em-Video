dados = []

for i in range(0, 5):
    dados.append(int(input(f'Digite o valor {i}: ')))

print(f'O maior valor foi {max(dados)}')
print(f'O menor valor foi {min(dados)}')

#-------------------------------------------------------------------------------------------------------------

dados = [] # variavel lista.
maior = menor = 0

for i in range(0, 5):  # Loop que vai gerar 5 inputs para colocar os valores.
    dados.append(int(input(f'Digite o valor {i}: ')))

    if i == 0:      
        maior = menor = dados[0]
    else:                       # A tomada de decisao que vai decidir o maior e o menor.
        if dados[i] > maior:
            maior = dados[i]
        if dados[i] < menor:
            menor = dados[i]

print(f'\nOs valores digitados foram: \033[31m{dados}\033[m') 
# Vai mostrar os valores contido na variavel "dados".

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(dados):
    if v == maior:
        print(f'{i}...', end='')
print()
# Vai mostrar o MAIOR valor na variavel "dados".

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(dados):
    if v == menor:
        print(f'{i}...', end='')
print()
# Vai mostrar o MENOR valor na variavel "dados"

